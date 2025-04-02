/******************************************************************************
 * ga_fuzzer.c
 *
 * Demonstrates a rough skeleton of how to implement a GA-based fuzzing loop
 * using AFL-style coverage bits, virgin_bits tracking, and a simplified MMD
 * distance for the fitness function.
 *
 * NOTE: This code is purely illustrative and omits many real AFL features.
 ******************************************************************************/

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <unistd.h>
#include <sys/shm.h>
#include <sys/wait.h>
#include <time.h>
#include <fcntl.h>
#include <dirent.h>
#include <sys/stat.h>
#include <errno.h>
#include <signal.h>


/* AFL-style definitions */
#define MAP_SIZE 65536
#define POP_SIZE 20
#define IND_SIZE 100
#define SELECT_SIZE 10
#define KEEP_SIZE 2
#define FORKSRV_FD 198
#define SHM_ENV_VAR  "__AFL_SHM_ID"

#define FS_NEW_VERSION_MIN 1
#define FS_NEW_VERSION_MAX 1
#define FS_NEW_ERROR 0xeffe0000
#define FS_NEW_OPT_MAPSIZE 0x00000001      // parameter: 32 bit value
#define FS_NEW_OPT_SHDMEM_FUZZ 0x00000002  // parameter: none
#define FS_NEW_OPT_AUTODICT 0x00000800     // autodictionary data




/* A global 'trace_bits' for coverage, and 'virgin_bits' to track never-before-hit edges. */
static uint8_t *trace_bits = NULL;
static uint8_t virgin_bits[MAP_SIZE]; /* Initialized to 0xFF at start */
static uint64_t total_execs;


/* We'll store the target's argv in a global. */
static char **target_argv = NULL;

static int shm_id = -1;

/* Store forkserver info in a global struct or in your own variables. */
static int fsrv_ctl_fd = -1; // control pipe
static int fsrv_st_fd  = -1; // status pipe
static int dev_null_fd = -1;
static int out_fd = -1;
static pid_t forksrv_pid = -1; // pid of the forkserver process
static uint8_t *out_file;



/* ---------------------------------------------------------------------------
 * Data structures
 * --------------------------------------------------------------------------- */

/* A single test case (analogous to a gene in GA). */
typedef struct {
    /* We'll store the file content. Alternatively, you can store just a path. */
    uint8_t *data;
    size_t size;
    /* We'll store coverage here after each run (copied from trace_bits). */
    uint8_t* coverage_ptr;
    uint8_t need_run;
    char *fname; /* optional: name/path if needed */
} TestCase;

/* Each Individual has multiple test cases (genes). */
typedef struct {
    TestCase *testcases;
    int tc_count;
    double fitness; /* We'll store the computed fitness (MMD distance, etc.) */
    uint8_t** coverage_r;
} Individual;

/* A population is just an array of individuals. */
typedef struct {
    Individual *individuals;
    int count;
} Population;



static Population *pop;
static Individual *seed_individual;

static void setup_stdio_file(void) {

    char* fn = ".cur_input";

    unlink(fn); /* Ignore errors */

    out_fd = open(fn, O_RDWR | O_CREAT | O_EXCL, 0600);

    if (out_fd < 0) printf("Unable to create '%s'\n", fn);

}

/* ---------------------------------------------------------------------------
 * Setup shared memory (AFL style). We do this once.
 * --------------------------------------------------------------------------- */
static int setup_shm(void) {
    shm_id = shmget(IPC_PRIVATE, MAP_SIZE, IPC_CREAT | IPC_EXCL | 0600);
    if (shm_id < 0) {
        perror("shmget");
        return -1;
    }

    trace_bits = shmat(shm_id, NULL, 0);
    if (trace_bits == (void *) -1) {
        perror("shmat");
        return -1;
    }

    memset(trace_bits, 0, MAP_SIZE);

    /* Set the AFL_SHM_ID in the environment so instrumented code can find it. */
    char shm_str[32];
    snprintf(shm_str, sizeof(shm_str), "%d", shm_id);
    setenv(SHM_ENV_VAR, shm_str, 1);



    return 0;
}

/* ---------------------------------------------------------------------------
 * Remove shared memory region.
 * --------------------------------------------------------------------------- */
static void remove_shm(void) {
    if (trace_bits && trace_bits != (void *) -1) {
        shmdt(trace_bits);
        trace_bits = NULL;
    }
    if (shm_id != -1) {
        shmctl(shm_id, IPC_RMID, NULL);
        shm_id = -1;
    }
}


/* Write modified data to file for testing. If out_file is set, the old file
   is unlinked and a new one is created. Otherwise, out_fd is rewound and
   truncated. */

static void write_to_testcase(void* mem, uint32_t len) {

    int fd = out_fd;

    if (out_file) {

        unlink(out_file); /* Ignore errors. */

        fd = open(out_file, O_WRONLY | O_CREAT | O_EXCL, 0600);

        if (fd < 0) printf("Unable to create '%s'", out_file);

    } else lseek(fd, 0, SEEK_SET);

    if (write(fd, mem, len) != len) {
        perror("write err");
    };

    if (!out_file) {
        if (ftruncate(fd, len)) perror("ftruncate() failed");
        lseek(fd, 0, SEEK_SET);

    } else
        close(fd);

}


static int start_forkserver(char** argv) {
    // setenv("AFL_OLD_FORKSERVER", "122", 1);
    int ctl_pipe[2], st_pipe[2];

    if (pipe(ctl_pipe) || pipe(st_pipe)) {
        perror("pipe");
        return -1;
    }

    forksrv_pid = fork();
    if (forksrv_pid < 0) {
        perror("fork");
        return -1;
    }

    if (forksrv_pid == 0) {
        /* CHILD: the forkserver process (actually, it's the target that
         * contains AFL's instrumentation) */

        // Set up the file descriptors for the forkserver (AFL forkserver protocol).
        // AFL expects that the child sees these fds on 198,199, but we'll keep it simpler:
        dup2(ctl_pipe[0], FORKSRV_FD);
        dup2(st_pipe[1], FORKSRV_FD + 1);


        dup2(dev_null_fd, 1);
        dup2(dev_null_fd, 2);

        if (out_file) {
            dup2(dev_null_fd, 0);

        } else {
            dup2(out_fd, 0);
            close(out_fd);
        }

        // We won't need the read end of st_pipe or the write end of ctl_pipe
        close(ctl_pipe[1]);
        close(st_pipe[0]);
        close(dev_null_fd);

        // In real AFL, the instrumentation in the target checks if
        // getpid() == the forkserver parent to confirm it's the server.

        // Exec the target in "forkserver mode."
        // printf("haha");


        execv(argv[0], argv);

        _exit(0);

    } else {
        /* PARENT: the fuzzer controlling the forkserver. */

        // We won't need the read end of ctl_pipe or the write end of st_pipe
        close(ctl_pipe[0]);
        close(st_pipe[1]);

        fsrv_ctl_fd = ctl_pipe[1];
        fsrv_st_fd  = st_pipe[0];

        // Wait for the forkserver to say "hello" (it writes a status int).
        int status = 0;
        int rlen = read(fsrv_st_fd, &status, 4);

        if (rlen == 4) {
            if ((status & FS_NEW_ERROR) == FS_NEW_ERROR) {
                fprintf(stderr, "FS_NEW_ERROR %d\n", WTERMSIG(status));
                _exit(1);

            }

            if (status >= 0x41464c00 && status <= 0x41464cff) {
                uint32_t version = status - 0x41464c00;
                if (!version) {

                    printf(
                        "Fork server version is not assigned, this should not happen. "
                        "Recompile target.");

                } else if (version < FS_NEW_VERSION_MIN || version > FS_NEW_VERSION_MAX) {

                    printf(
                        "Fork server version is not not supported.  Recompile the target.");

                }
                uint32_t keep = status;
                status ^= 0xffffffff;
                if (write(fsrv_ctl_fd, &status, 4) != 4) {

                    printf("Writing to forkserver failed.");

                }

                printf("All right - new fork server model v%u is up.\n", version);

                rlen = read(fsrv_st_fd, &status, 4);
                printf("Forkserver options received: (0x%08x)\n", status);

                if (status & FS_NEW_OPT_MAPSIZE) {

                    uint32_t tmp_map_size;
                    rlen = read(fsrv_st_fd, &tmp_map_size, 4);

                    if (tmp_map_size % 64) {

                        tmp_map_size = (((tmp_map_size + 63) >> 6) << 6);

                    }

                    if (tmp_map_size > MAP_SIZE) {

                        printf(
                            "Target's coverage map size of %u is larger than the one this "
                            "AFL++ is set with (%u). Either set AFL_MAP_SIZE=%u and "
                            "restart "
                            " afl-fuzz, or change MAP_SIZE_POW2 in config.h and recompile "
                            "afl-fuzz",
                            tmp_map_size, MAP_SIZE, tmp_map_size);

                    }
                } else {

                }

                uint32_t status2;
                rlen = read(fsrv_st_fd, &status2, 4);

                if (status2 != keep) {

                    printf("Error in forkserver communication (%08x=>%08x)", keep, status2);

                }

            }



            return 0;
        }

        if (waitpid(forksrv_pid, &status, 0) <= 0)
            fprintf(stderr, "waitpid() failed\n");

        if (WIFSIGNALED(status)) {
            fprintf(stderr, "Fork server crashed with signal %d\n", WTERMSIG(status));
        }

        if (status) {
            fprintf(stderr, "Forkserver reported an error. status=%u\n", status);
            return -1;
        }
        fprintf(stderr, "Forkserver started successfully (PID = %d)\n", forksrv_pid);
    }

    return 0;
}


/* ---------------------------------------------------------------------------
 * init_virgin_bits: set all virgin_bits to 0xFF (meaning all edges are
 * "unseen" initially).
 * --------------------------------------------------------------------------- */
static void init_virgin_bits(void) {
    memset(virgin_bits, 0xFF, MAP_SIZE);
}


/* ---------------------------------------------------------------------------
 * mutate_testcase: apply a simple AFL-style mutation to a single test case.
 * (You could also implement the earlier 'mutate_seed()' logic here.)
 * --------------------------------------------------------------------------- */
static void mutate_testcase(TestCase *tc) {
    if (tc->size == 0) return;
    tc->need_run = 1;
    /* Example: flip a random bit. */
    int pos = rand() % tc->size;
    int bit = rand() % 8;
    tc->data[pos] ^= (1 << bit);
}

/* ---------------------------------------------------------------------------
 * load_seed_files: read all files from a seed directory, create an
 * "Individual" that holds them. This might form your "seed individual."
 * --------------------------------------------------------------------------- */
static Individual* load_seed_files(const char *seed_dir) {
    Individual *seed_indiv = malloc(sizeof(Individual));
    memset(seed_indiv, 0, sizeof(Individual));

    DIR *d = opendir(seed_dir);
    if (!d) {
        perror("opendir");
        return seed_indiv; /* returns an empty individual if error */
    }

    /* We’ll store testcases in a dynamic array (realloc). */
    TestCase *tcs = NULL;
    int count = 0;

    struct dirent *de;
    while ((de = readdir(d)) != NULL) {
        if (de->d_name[0] == '.') continue; /* skip '.' or hidden files */

        /* Build full path */
        char path[1024];
        snprintf(path, sizeof(path), "%s/%s", seed_dir, de->d_name);

        /* Check if it's a file. */
        struct stat st;
        if (stat(path, &st) == 0 && S_ISREG(st.st_mode)) {
            /* Load file content into memory. */
            FILE *f = fopen(path, "rb");
            if (!f) {
                perror("fopen");
                continue;
            }
            fseek(f, 0, SEEK_END);
            long fsize = ftell(f);
            fseek(f, 0, SEEK_SET);

            if (fsize <= 0) {
                fclose(f);
                continue;
            }

            uint8_t *buf = malloc(fsize);
            if (!buf) {
                perror("malloc");
                fclose(f);
                continue;
            }
            fread(buf, 1, fsize, f);
            fclose(f);

            /* Expand testcases array */
            tcs = realloc(tcs, (count + 1) * sizeof(TestCase));
            tcs[count].data = buf;
            tcs[count].size = fsize;
            tcs[count].need_run = 1;
            tcs[count].coverage_ptr = malloc(MAP_SIZE);
            tcs[count].fname = strdup(de->d_name); /* store filename, optional */
            count++;
        }
    }

    closedir(d);

    /* 3) If count < IND_SIZE, supplement by mutating existing testcases. */
    while (count < IND_SIZE && count > 0) {
        /* Randomly pick one of the already loaded testcases. */
        int rand_idx = rand() % count;

        /* Duplicate the data buffer. */
        size_t new_size = tcs[rand_idx].size;
        uint8_t* new_buf = malloc(new_size);
        if (!new_buf) {
            perror("malloc new_buf");
            break; /* We'll just stop if allocation fails. */
        }
        memcpy(new_buf, tcs[rand_idx].data, new_size);

        /* Append new_tc to tcs array. */
        tcs = realloc(tcs, (count + 1) * sizeof(TestCase));
        if (!tcs) {
            perror("realloc tcs for new testcase");
            /* Free new_tc.data if you want to avoid leaks. */
            free(new_buf);
            break;
        }

        /* Create a new TestCase struct and mutate it. */

        tcs[count].data  = new_buf;
        tcs[count].size  = new_size;
        tcs[count].need_run = 1;
        /* coverage_ptr remains NULL for now; set after run. */
        tcs[count].fname = NULL;  /* or "mutated" if you prefer */
        tcs[count].coverage_ptr = malloc(MAP_SIZE);

        /* Mutate. */
        mutate_testcase(&tcs[count]);

        count++;
    }

    seed_indiv->testcases = tcs;
    seed_indiv->tc_count = count;
    seed_indiv->coverage_r = calloc(count, sizeof(uint8_t*));
    seed_indiv->fitness = 0.0;
    return seed_indiv;
}

// /* ---------------------------------------------------------------------------
//  * run_testcase: uses fork+exec to run the target with the given testcase
//  * (redirect data to stdin). Clears trace_bits, runs, returns success/fail.
//  * --------------------------------------------------------------------------- */
// static int run_testcase(const TestCase *tc) {
//     /* Clear trace_bits first */
//     memset(trace_bits, 0, MAP_SIZE);
//
//     pid_t pid = fork();
//     if (pid < 0) {
//         perror("fork");
//         return -1;
//     }
//
//     if (pid == 0) {
//         /* Child */
//         /* We'll pipe the test case data to stdin. */
//         int pipefd[2];
//         if (pipe(pipefd) < 0) {
//             perror("pipe");
//             _exit(1);
//         }
//
//         pid_t writer = fork();
//         if (writer < 0) {
//             perror("fork writer");
//             _exit(1);
//         }
//
//         if (writer == 0) {
//             /* Grandchild writes data to pipe */
//             close(pipefd[0]);
//             write(pipefd[1], tc->data, tc->size);
//             close(pipefd[1]);
//             _exit(0);
//         } else {
//             /* Child reads from pipe on stdin */
//             close(pipefd[1]);
//             dup2(pipefd[0], STDIN_FILENO);
//             close(pipefd[0]);
//
//             int fd = open("/dev/null", O_WRONLY);
//
//             dup2(fd, 1);    /* make stdout a copy of fd (> /dev/null) */
//             dup2(fd, 2);    /* ...and same with stderr */
//             close(fd);
//
//             /* Exec the instrumented target (global var target_argv, for instance). */
//             /* In a real fuzzer, you'd have set target_argv[] previously. */
//
//             execv(target_argv[0], target_argv);
//             perror("execv");
//             _exit(1);
//         }
//     } else {
//         /* Parent */
//         int status = 0;
//         waitpid(pid, &status, 0);
//
//         if (WIFSIGNALED(status) || WIFEXITED(status)) {
//             printf("child exited with status of %d\n", WEXITSTATUS(status));
//             return -1;
//         }
//
//         return 0;
//     }
// }


static int run_testcase_forkserver(const TestCase* tc) {

    write_to_testcase(tc->data, tc->size);
    // 2) Zero out trace_bits
    memset(trace_bits, 0, MAP_SIZE);

    // 3) Send forkserver the "run" command
    // AFL usually sends a 4-byte integer, e.g. 0 or 0xFFFFFFFF

    unsigned int status =0 ;
    int res;
    static uint32_t prev_timed_out = 1;

    if ((res = write(fsrv_ctl_fd, &prev_timed_out, 4)) != 4) {

        printf("Unable to request new process from fork server (OOM?)\n");

    }




    // 4) Read child PID from fsrv_st_fd
    unsigned int child_pid;
    if (read(fsrv_st_fd, &child_pid, 4) != 4) {
        fprintf(stderr, "Unable to request new process from fork server (OOM?)\n");
        return -1;
    }

    if (child_pid <= 0) {
        // The forkserver indicated an error in fork() or similar
        fprintf(stderr, "Forkserver reported a fork error.\n");
        return -1;
    }

    // 5) Read status

    if (read(fsrv_st_fd, &status, 4) != 4) {
        fprintf(stderr, "Failed to read child exit status from forkserver.\n");
        return -1;
    }

    if (!WIFSTOPPED(status))
        child_pid = 0;
    total_execs++;
    // success
    return 0;
}



/* ---------------------------------------------------------------------------
 * update_virgin_bits: for each coverage byte in 'coverage_map', if there's a
 * new edge (trace_bits[i] != 0 && virgin_bits[i] == 0xFF), we update it.
 * *new_bits_found is set to 1 if any new coverage was discovered.
 * --------------------------------------------------------------------------- */
static void update_virgin_bits(const uint8_t *coverage_map, int *new_bits_found) {
    int found = 0;
    for (int i = 0; i < MAP_SIZE; i++) {
        if (coverage_map[i] && virgin_bits[i] == 0xFF) {
            virgin_bits[i] = coverage_map[i]; /* or 0x00 to mark it as discovered */
            found = 1;
        }
    }
    if (found && new_bits_found) {
        *new_bits_found = 1;
    }
}

/* ---------------------------------------------------------------------------
 * collect_coverage_for_individual:
 *
 * 1) For each test in 'indiv':
 *    - run_testcase() to populate trace_bits
 *    - allocate coverage_ptr = malloc(MAP_SIZE)
 *    - copy trace_bits -> coverage_ptr
 *    - update virgin_bits to track newly discovered coverage
 *
 * 2) Return a newly allocated 2D array coverage2D, where coverage2D[i] is
 *    also a copy of trace_bits for test i. This is often redundant with
 *    coverage_ptr, but shows how you might return a 2D coverage structure.
 *
 * Caller must free coverage2D[i] and coverage2D when done.
 * --------------------------------------------------------------------------- */
static void run_individual(Individual* indiv) {

    for (int i = 0; i < indiv->tc_count; i++) {
        if (indiv->testcases[i].need_run == 0) {
            indiv->coverage_r[i] = indiv->testcases[i].coverage_ptr;
            continue;
        }


        if (run_testcase_forkserver(&indiv->testcases[i]) < 0) {
            // If crashed or error, still allocate coverage but zero it out
            indiv->testcases[i].coverage_ptr = NULL;
            continue;
        }

        int coverage = 0;
        for (int i = 0; i < MAP_SIZE; i++) {
            if (trace_bits[i]) coverage++;
        }

        memcpy(indiv->testcases[i].coverage_ptr, trace_bits, MAP_SIZE);

        // Also record in indiv
        indiv->coverage_r[i] = indiv->testcases[i].coverage_ptr;

        // Update global virgin_bits to track new coverage
        int new_bits_found = 0;
        update_virgin_bits(trace_bits, &new_bits_found);
        if (new_bits_found) {
            // Optionally save interesting cases, etc.
        }
    }
}


/* ---------------------------------------------------------------------------
 * compute_mmd_distance: a placeholder function that compares two distributions
 * dist_a, dist_b (each size MAP_SIZE). Real MMD requires more sophisticated
 * kernel-based or sample-based methods. We'll do a toy difference measure.
 * --------------------------------------------------------------------------- */
static double compute_mmd_distance(const uint8_t** *dist_a, const uint8_t** *dist_b) {
    double sum_diff = 0.0;
    return sum_diff;
}




/* ---------------------------------------------------------------------------
 * crossover_individuals: given two parents, produce a child by mixing testcases.
 * You can also do crossover within testcases, etc.
 * --------------------------------------------------------------------------- */
static void crossover_individuals(const Individual *parent1,
                                  const Individual *parent2,
                                  Individual *child) {

    /* For simplicity, let child have the same number of testcases as parent1. */
    child->tc_count = parent1->tc_count;

    for (int i = 0; i < child->tc_count; i++) {

        /* 50% chance from p1 or p2. Then duplicate the data buffer. */
        const TestCase *source =
                (rand() % 2) ? &parent1->testcases[i] : &parent2->testcases[i];
        child->testcases[i].size = source->size;

        child->testcases[i].data = malloc(source->size);
        memcpy(child->testcases[i].data, source->data, source->size);


        child->testcases[i].need_run = 0;


        memcpy(child->testcases[i].coverage_ptr, source->coverage_ptr, MAP_SIZE);
        child->testcases[i].fname = NULL;

    }
}

/* ---------------------------------------------------------------------------
 * ga_evolve_population: the core GA steps in a simplified form:
 *   1) compute distributions & fitness for each indiv
 *   2) rank/sort
 *   3) crossover + mutation -> new population
 * --------------------------------------------------------------------------- */
static void ga_evolve_population() {
    /* 1) Evaluate each individual's distribution + fitness. */
    for (int i = 0; i < pop->count; i++) {
        /* compute distribution for individual i */
        double dist[MAP_SIZE];

        run_individual(&pop->individuals[i]);

        /* measure MMD distance from seed_distribution */
        double mmd = compute_mmd_distance(&pop->individuals[i].coverage_r, seed_individual->coverage_r);
        pop->individuals[i].fitness = mmd;
    }

    /* 2) Sort the population by descending fitness. (largest = best) */
    for (int i = 0; i < pop->count - 1; i++) {
        for (int j = i + 1; j < pop->count; j++) {
            if (pop->individuals[j].fitness > pop->individuals[i].fitness) {
                Individual tmp = pop->individuals[i];
                pop->individuals[i] = pop->individuals[j];
                pop->individuals[j] = tmp;
            }
        }
    }


    /* 3) For demonstration, we do a simple "replace the bottom half with children." */

    for (int i = KEEP_SIZE; i < pop->count; i++) {
        /* pick 2 parents from the top half, produce a child. */
        int p1 = rand() % SELECT_SIZE;
        int p2 = rand() % SELECT_SIZE;
        if (p2 == p1)
            p2 = p1 + 1;

        /* free the old individual's testcases */
        for (int t = 0; t < pop->individuals[i].tc_count; t++) {
            free(pop->individuals[i].testcases[t].data);
            free(pop->individuals[i].testcases[t].fname);
        }



        pop->individuals[i].fitness = 0;

        crossover_individuals(&pop->individuals[p1], &pop->individuals[p2],
                              &pop->individuals[i]);

        /* Then mutate some testcases in the child. */
        for (int t = 0; t < pop->individuals[i].tc_count; t++) {
            /* small chance each testcase gets mutated. */
            if (rand() % 100 < 50) {
                mutate_testcase(&pop->individuals[i].testcases[t]);
            }
        }
    }
}

/* -------------------------------------------------------------------------
 * init_population - Create a population of size 'count' from a seed individual.
 *
 * For each new Individual in the population:
 *   - Copy the seed's test cases.
 *   - For each test case in the seed, call 'mutate_testcase()' N times
 *     (where N = count), producing a single mutated version of that seed test.
 *   - Store the mutated test in the new individual's test array.
 *
 * Signature:
 *   Pop* init_population(Individual* ind, int count);
 *
 * Parameters:
 *   ind   - pointer to the seed individual (with testcases)
 *   count - the number of Individuals to create in the population.
 *           Also used as the number of repeated mutations per test.
 *
 * Returns:
 *   A pointer to a newly allocated Pop structure. The caller must eventually
 *   free the memory.
 * ------------------------------------------------------------------------- */
Population* init_population(Individual* ind, int count) {
    /* 1) Allocate the population. */
    Population* pop = (Population*)malloc(sizeof(Population));
    if (!pop) {
        perror("malloc Pop");
        return NULL;
    }
    pop->count = count;


    /* 2) Allocate the array of Individuals. */
    pop->individuals = (Individual*)calloc(count, sizeof(Individual));
    if (!pop->individuals) {
        perror("calloc Individuals");
        free(pop);
        return NULL;
    }

    /* 3) For each Individual in the population: */
    for (int i = 0; i < count; i++) {
        /* Allocate an array of testcases matching seed's count. */
        pop->individuals[i].tc_count  = ind->tc_count;
        pop->individuals[i].fitness = 0.0;
        pop->individuals[i].coverage_r = calloc(ind->tc_count, sizeof(uint8_t*));
        pop->individuals[i].testcases = (TestCase*)calloc(ind->tc_count, sizeof(TestCase));
        if (!pop->individuals[i].testcases) {
            perror("calloc testcases");
            /* A real implementation would clean up previous allocations. */
            /* For brevity, we omit a full cleanup routine here. */
            return pop;
        }

        /* 4) For each test case in the seed, copy + mutate it. */
        for (int t = 0; t < ind->tc_count; t++) {
            /* Copy the seed test's data buffer. */
            size_t sz = ind->testcases[t].size;
            pop->individuals[i].testcases[t].size = sz;
            pop->individuals[i].testcases[t].data = (uint8_t*)malloc(sz);
            pop->individuals[i].testcases[t].fname = NULL;
            pop->individuals[i].testcases[t].coverage_ptr = malloc(MAP_SIZE);
            memset(pop->individuals[i].testcases[t].coverage_ptr, 0, MAP_SIZE);
            pop->individuals[i].testcases[t].need_run = 1;
            if (!pop->individuals[i].testcases[t].data) {
                perror("malloc test data");
                /* Proper cleanup omitted for brevity. */
                return pop;
            }
            /* Copy seed bytes. */
            memcpy(pop->individuals[i].testcases[t].data,
                   ind->testcases[t].data, sz);

            mutate_testcase(&pop->individuals[i].testcases[t]);

        }
    }

    return pop;
}

static void free_individual(Individual* ind) {
    if (ind != NULL) {
        for (int i = 0; i < ind->tc_count; i++) {
            free(ind->testcases[i].data);
            free(ind->testcases[i].fname);
            free(ind->testcases[i].coverage_ptr);
        }
        free(ind->testcases);
        free(ind->coverage_r);
        // free(ind);
    }
}

/* ---------------------------------------------------------------------------
 * main demonstration
 * --------------------------------------------------------------------------- */
int main(int argc, char **argv) {
    if (argc < 3) {
        fprintf(stderr,
          "Usage: %s <instrumented_target> [target_args ...] <seed_dir>\n"
          "Example:\n"
          "  %s ./instrumented_target -x 123 seeds/\n"
          "The last argument is a directory containing seed files.\n",
          argv[0], argv[0]);
        return 1;
    }

    // The seed directory is the last argument
    const char* seed_dir = argv[argc - 1];
    total_execs = 0;

    // Everything between argv[1] and argv[argc - 2] belongs to the target:
    //   argv[1] = <instrumented_target>
    //   argv[2..(argc-2)] = optional arguments
    int target_argc = argc - 2; // number of args for the target
    target_argv = (char**)calloc(target_argc + 1, sizeof(char*));
    if (!target_argv) {
        perror("calloc target_argv");
        return 1;
    }

    // Copy the target args into target_argv, and terminate with NULL
    for (int i = 0; i < target_argc; i++) {
        target_argv[i] = argv[i + 1];  // shift by 1 to skip our own binary name
    }
    target_argv[target_argc] = NULL; // required for execv



    srand((unsigned) time(NULL));

    if (!out_file) setup_stdio_file();

    dev_null_fd = open("/dev/null", O_RDWR);
    if (dev_null_fd < 0) perror("Unable to open /dev/null");

    // 1) Setup shared memory
    if (setup_shm() < 0) {
        fprintf(stderr, "Failed to setup shared memory.\n");
        free(target_argv);
        return 1;
    }

    if (start_forkserver(target_argv) < 0) {
        fprintf(stderr, "Failed to start forkserver.\n");
        // cleanup etc
        free(target_argv);
        return 1;
    }
    init_virgin_bits();


    // 2) Load seeds from 'seed_dir' into an Individual (example)
    printf("===  Load Files =====\n");
    seed_individual = load_seed_files(seed_dir);
    printf("===  Dry Run =====\n");
    run_individual(seed_individual); //get initial coverage

    if (seed_individual->tc_count == 0) {
        fprintf(stderr, "No seed files loaded from directory: %s\n", seed_dir);
        remove_shm();
        free(target_argv);
        // free individual?
        return 1;
    }




    /* 4) Create an initial population. E.g., replicate seed_indiv multiple times,
     * or mutate them. We'll do a small population of size 4 for demo. */
    printf("===  Initilize Pop =====\n");
    pop = init_population(seed_individual, POP_SIZE);

    /* 5) GA main loop: run a few generations. */
    int generations = 5; /* just for demonstration */
    for (int gen = 0; gen < generations; gen++) {
        printf("=== Generation %d ===\n", gen);
        ga_evolve_population();
        printf("Best fitness so far: %f\n", pop->individuals[0].fitness);
    }

    /* 6) Cleanup. */
    /* Free seed_indiv testcases. */
    free_individual(seed_individual);

    /* Free pop. */
    for (int i = 0; i < pop->count; i++) {
        free_individual(&pop->individuals[i]);
    }
    free(pop->individuals);
    free(pop);

    remove_shm();
    free(target_argv);

    if (forksrv_pid > 0) kill(forksrv_pid, SIGKILL);
    return 0;
}
