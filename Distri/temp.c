for id in $(ipcs -m | awk 'NR>3 {print $2}'); do
    ipcrm -m $id
done



/******************************************************************************
 * ga_fuzzer.c
 *
 * Demonstrates how to:
 *  - Parse arguments for an instrumented target and a seed directory.
 *  - Set up AFL-style coverage shared memory (trace_bits).
 *  - Store coverage for each test case by copying from trace_bits (no overwrite).
 *  - Return a 2D coverage array from collect_coverage_for_individual().
 *  - Compute a distribution from the per-test coverage data.
 *
 * This is a minimal skeleton and omits many real-world fuzzer features.
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

#define MAP_SIZE    65536
#define SHM_ENV_VAR "AFL_SHM_ID"

/* Global coverage map pointer. Instrumented target will write here. */
static uint8_t* trace_bits = NULL;
static int shm_id = -1;

/* AFL-style "virgin_bits" to track global coverage not yet discovered. */
static uint8_t virgin_bits[MAP_SIZE];

/* We'll store the instrumented target's argv in this global for exec. */
static char** target_argv = NULL;

/* ---------------------------------------------------------------------------
 * Data structures
 * --------------------------------------------------------------------------- */

/* Each TestCase has data, size, plus a coverage_ptr that *copies* trace_bits. */
typedef struct {
    uint8_t* data;
    size_t   size;

    /* We'll store coverage here after each run (copied from trace_bits). */
    uint8_t* coverage_ptr;
} TestCase;

/* An Individual: a collection of test cases. */
typedef struct {
    TestCase* testcases;
    int       tc_count;
} Individual;

/* ---------------------------------------------------------------------------
 * Shared Memory Setup & Teardown
 * --------------------------------------------------------------------------- */
static int setup_shm(void) {
    shm_id = shmget(IPC_PRIVATE, MAP_SIZE, IPC_CREAT | IPC_EXCL | 0600);
    if (shm_id < 0) {
        perror("shmget");
        return -1;
    }
    trace_bits = shmat(shm_id, NULL, 0);
    if (trace_bits == (void*)-1) {
        perror("shmat");
        return -1;
    }
    memset(trace_bits, 0, MAP_SIZE);

    /* Set the AFL_SHM_ID for the instrumented target to pick up. */
    char shm_str[32];
    snprintf(shm_str, sizeof(shm_str), "%d", shm_id);
    setenv(SHM_ENV_VAR, shm_str, 1);

    return 0;
}

static void remove_shm(void) {
    if (trace_bits && trace_bits != (void*)-1) {
        shmdt(trace_bits);
        trace_bits = NULL;
    }
    if (shm_id != -1) {
        shmctl(shm_id, IPC_RMID, NULL);
        shm_id = -1;
    }
}

/* ---------------------------------------------------------------------------
 * init_virgin_bits: sets all edges to 0xFF => "unseen."
 * --------------------------------------------------------------------------- */
static void init_virgin_bits(void) {
    memset(virgin_bits, 0xFF, MAP_SIZE);
}

/* ---------------------------------------------------------------------------
 * update_virgin_bits: If we see a coverage byte in trace_bits that was 0xFF
 * in virgin_bits, we mark it as discovered and set *new_bits_found = 1.
 * --------------------------------------------------------------------------- */
static void update_virgin_bits(const uint8_t* coverage_map, int* new_bits_found) {
    int found = 0;
    for (int i = 0; i < MAP_SIZE; i++) {
        if (coverage_map[i] && virgin_bits[i] == 0xFF) {
            /* Mark discovered. Could store coverage_map[i], or just 0x00. */
            virgin_bits[i] = coverage_map[i];
            found = 1;
        }
    }
    if (found && new_bits_found) {
        *new_bits_found = 1;
    }
}

/* ---------------------------------------------------------------------------
 * run_testcase: forks, pipes testcase data to child's stdin, execs target.
 * --------------------------------------------------------------------------- */
static int run_testcase(const TestCase* tc) {
    /* Clear trace_bits so we only see coverage from this run. */
    memset(trace_bits, 0, MAP_SIZE);

    pid_t pid = fork();
    if (pid < 0) {
        perror("fork");
        return -1;
    }

    if (pid == 0) {
        /* Child process */
        int pipefd[2];
        if (pipe(pipefd) < 0) {
            perror("pipe");
            _exit(1);
        }

        pid_t writer = fork();
        if (writer < 0) {
            perror("fork writer");
            _exit(1);
        }

        if (writer == 0) {
            /* Grandchild writes data to pipe. */
            close(pipefd[0]);
            write(pipefd[1], tc->data, tc->size);
            close(pipefd[1]);
            _exit(0);
        } else {
            /* Child reads from pipe on stdin. */
            close(pipefd[1]);
            dup2(pipefd[0], STDIN_FILENO);
            close(pipefd[0]);

            /* Exec the instrumented target (using global target_argv). */
            execv(target_argv[0], target_argv);
            perror("execv");
            _exit(1);
        }
    } else {
        /* Parent process */
        int status;
        waitpid(pid, &status, 0);
        if (WIFSIGNALED(status) || WEXITSTATUS(status) != 0) {
            /* Crash or non-zero exit */
            return -1;
        }
        return 0; /* success */
    }
}

/* ---------------------------------------------------------------------------
 * load_seed_files: loads all files in 'seed_dir' into a single Individual.
 * Each file becomes one test case with data. coverage_ptr is initially NULL.
 * --------------------------------------------------------------------------- */
static Individual load_seed_files(const char* seed_dir) {
    Individual indiv;
    memset(&indiv, 0, sizeof(Individual));

    DIR* d = opendir(seed_dir);
    if (!d) {
        perror("opendir");
        return indiv; // returns empty if error
    }

    TestCase* tcs = NULL;
    int count = 0;

    struct dirent* de;
    while ((de = readdir(d)) != NULL) {
        if (de->d_name[0] == '.') continue; // skip '.' or hidden

        char path[1024];
        snprintf(path, sizeof(path), "%s/%s", seed_dir, de->d_name);

        struct stat st;
        if (stat(path, &st) == 0 && S_ISREG(st.st_mode)) {
            FILE* f = fopen(path, "rb");
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

            uint8_t* buf = malloc(fsize);
            if (!buf) {
                perror("malloc");
                fclose(f);
                continue;
            }
            fread(buf, 1, fsize, f);
            fclose(f);

            // Expand testcases array
            tcs = realloc(tcs, (count + 1) * sizeof(TestCase));
            tcs[count].data         = buf;
            tcs[count].size         = fsize;
            tcs[count].coverage_ptr = NULL;  // set after run
            count++;
        }
    }
    closedir(d);

    indiv.testcases = tcs;
    indiv.tc_count  = count;
    return indiv;
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
 * Caller must free coverage2D[i] and coverage2D when don
/******************************************************************************
 * ga_fuzzer.c
 *
 * Demonstrates how to:
 *  - Parse arguments for an instrumented target and a seed directory.
 *  - Set up AFL-style coverage shared memory (trace_bits).
 *  - Store coverage for each test case by copying from trace_bits (no overwrite).
 *  - Return a 2D coverage array from collect_coverage_for_individual().
 *  - Compute a distribution from the per-test coverage data.
 *
 * This is a minimal skeleton and omits many real-world fuzzer features.
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

#define MAP_SIZE    65536
#define SHM_ENV_VAR "AFL_SHM_ID"

/* Global coverage map pointer. Instrumented target will write here. */
static uint8_t* trace_bits = NULL;
static int shm_id = -1;

/* AFL-style "virgin_bits" to track global coverage not yet discovered. */
static uint8_t virgin_bits[MAP_SIZE];

/* We'll store the instrumented target's argv in this global for exec. */
static char** target_argv = NULL;

/* ---------------------------------------------------------------------------
 * Data structures
 * --------------------------------------------------------------------------- */

/* Each TestCase has data, size, plus a coverage_ptr that *copies* trace_bits. */
typedef struct {
    uint8_t* data;
    size_t   size;

    /* We'll store coverage here after each run (copied from trace_bits). */
    uint8_t* coverage_ptr;
} TestCase;

/* An Individual: a collection of test cases. */
typedef struct {
    TestCase* testcases;
    int       tc_count;
} Individual;

/* ---------------------------------------------------------------------------
 * Shared Memory Setup & Teardown
 * --------------------------------------------------------------------------- */
static int setup_shm(void) {
    shm_id = shmget(IPC_PRIVATE, MAP_SIZE, IPC_CREAT | IPC_EXCL | 0600);
    if (shm_id < 0) {
        perror("shmget");
        return -1;
    }
    trace_bits = shmat(shm_id, NULL, 0);
    if (trace_bits == (void*)-1) {
        perror("shmat");
        return -1;
    }
    memset(trace_bits, 0, MAP_SIZE);

    /* Set the AFL_SHM_ID for the instrumented target to pick up. */
    char shm_str[32];
    snprintf(shm_str, sizeof(shm_str), "%d", shm_id);
    setenv(SHM_ENV_VAR, shm_str, 1);

    return 0;
}

static void remove_shm(void) {
    if (trace_bits && trace_bits != (void*)-1) {
        shmdt(trace_bits);
        trace_bits = NULL;
    }
    if (shm_id != -1) {
        shmctl(shm_id, IPC_RMID, NULL);
        shm_id = -1;
    }
}

/* ---------------------------------------------------------------------------
 * init_virgin_bits: sets all edges to 0xFF => "unseen."
 * --------------------------------------------------------------------------- */
static void init_virgin_bits(void) {
    memset(virgin_bits, 0xFF, MAP_SIZE);
}

/* ---------------------------------------------------------------------------
 * update_virgin_bits: If we see a coverage byte in trace_bits that was 0xFF
 * in virgin_bits, we mark it as discovered and set *new_bits_found = 1.
 * --------------------------------------------------------------------------- */
static void update_virgin_bits(const uint8_t* coverage_map, int* new_bits_found) {
    int found = 0;
    for (int i = 0; i < MAP_SIZE; i++) {
        if (coverage_map[i] && virgin_bits[i] == 0xFF) {
            /* Mark discovered. Could store coverage_map[i], or just 0x00. */
            virgin_bits[i] = coverage_map[i];
            found = 1;
        }
    }
    if (found && new_bits_found) {
        *new_bits_found = 1;
    }
}

/* ---------------------------------------------------------------------------
 * run_testcase: forks, pipes testcase data to child's stdin, execs target.
 * --------------------------------------------------------------------------- */
static int run_testcase(const TestCase* tc) {
    /* Clear trace_bits so we only see coverage from this run. */
    memset(trace_bits, 0, MAP_SIZE);

    pid_t pid = fork();
    if (pid < 0) {
        perror("fork");
        return -1;
    }

    if (pid == 0) {
        /* Child process */
        int pipefd[2];
        if (pipe(pipefd) < 0) {
            perror("pipe");
            _exit(1);
        }

        pid_t writer = fork();
        if (writer < 0) {
            perror("fork writer");
            _exit(1);
        }

        if (writer == 0) {
            /* Grandchild writes data to pipe. */
            close(pipefd[0]);
            write(pipefd[1], tc->data, tc->size);
            close(pipefd[1]);
            _exit(0);
        } else {
            /* Child reads from pipe on stdin. */
            close(pipefd[1]);
            dup2(pipefd[0], STDIN_FILENO);
            close(pipefd[0]);

            /* Exec the instrumented target (using global target_argv). */
            execv(target_argv[0], target_argv);
            perror("execv");
            _exit(1);
        }
    } else {
        /* Parent process */
        int status;
        waitpid(pid, &status, 0);
        if (WIFSIGNALED(status) || WEXITSTATUS(status) != 0) {
            /* Crash or non-zero exit */
            return -1;
        }
        return 0; /* success */
    }
}

/* ---------------------------------------------------------------------------
 * load_seed_files: loads all files in 'seed_dir' into a single Individual.
 * Each file becomes one test case with data. coverage_ptr is initially NULL.
 * --------------------------------------------------------------------------- */
static Individual load_seed_files(const char* seed_dir) {
    Individual indiv;
    memset(&indiv, 0, sizeof(Individual));

    DIR* d = opendir(seed_dir);
    if (!d) {
        perror("opendir");
        return indiv; // returns empty if error
    }

    TestCase* tcs = NULL;
    int count = 0;

    struct dirent* de;
    while ((de = readdir(d)) != NULL) {
        if (de->d_name[0] == '.') continue; // skip '.' or hidden

        char path[1024];
        snprintf(path, sizeof(path), "%s/%s", seed_dir, de->d_name);

        struct stat st;
        if (stat(path, &st) == 0 && S_ISREG(st.st_mode)) {
            FILE* f = fopen(path, "rb");
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

            uint8_t* buf = malloc(fsize);
            if (!buf) {
                perror("malloc");
                fclose(f);
                continue;
            }
            fread(buf, 1, fsize, f);
            fclose(f);

            // Expand testcases array
            tcs = realloc(tcs, (count + 1) * sizeof(TestCase));
            tcs[count].data         = buf;
            tcs[count].size         = fsize;
            tcs[count].coverage_ptr = NULL;  // set after run
            count++;
        }
    }
    closedir(d);

    indiv.testcases = tcs;
    indiv.tc_count  = count;
    return indiv;
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
 * Caller must free coverage2D[i] and coverage2D when don
//
// Created by XIE Xiaofei on 26/2/25.
//
