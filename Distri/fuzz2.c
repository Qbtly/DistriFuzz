/******************************************************************************
 * mini_fuzzer.c
 *
 * - Defines SHM_ENV_VAR as "AFL_SHM_ID" (following AFL convention).
 * - Sets the environment variable once in setup_shm().
 * - The child processes inherit AFL_SHM_ID, so the instrumented code can write
 *   coverage to trace_bits.
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
#include <errno.h>
#include <sys/stat.h>

/* Coverage map size (AFL default is 65536). */
#define MAP_SIZE 65536

/* AFL environment variable for shared memory ID. */
#define SHM_ENV_VAR  "__AFL_SHM_ID"

static uint8_t *trace_bits = NULL;
static int shm_id = -1;

/* We'll store the target's argv in a global. */
static char **target_argv = NULL;

/* -------------------------------------------------------------------------
 * setup_shm: Create and attach to a SysV shared memory region for coverage.
 * Set the environment variable SHM_ENV_VAR so the instrumented target sees it.
 * ------------------------------------------------------------------------- */
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

    /* Clear at startup. */
    memset(trace_bits, 0, MAP_SIZE);

    /* Convert shm_id to string and set it as AFL_SHM_ID in environment. */
    char shm_str[32];
    snprintf(shm_str, sizeof(shm_str), "%d", shm_id);
    setenv(SHM_ENV_VAR, shm_str, 1);

    return 0;
}

/* -------------------------------------------------------------------------
 * remove_shm: Destroy the shared memory (AFL does this upon exit).
 * ------------------------------------------------------------------------- */
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

/* -------------------------------------------------------------------------
 * setup_stdio_file: Redirect the seed file to stdin for the target.
 * ------------------------------------------------------------------------- */
static int setup_stdio_file(const char *seed_path) {
    int fd = open(seed_path, O_RDONLY);
    if (fd < 0) {
        perror("open seed_path");
        return -1;
    }

    if (dup2(fd, STDIN_FILENO) < 0) {
        perror("dup2");
        close(fd);
        return -1;
    }

    close(fd);
    return 0;
}

/* -------------------------------------------------------------------------
 * run_seed:
 *  1) Clears trace_bits.
 *  2) Forks. The child:
 *     - inherits AFL_SHM_ID from environment
 *     - redirects seed file -> stdin
 *     - execv(target_argv[0], target_argv)
 *  3) Parent waits, then counts coverage in trace_bits.
 *  4) Returns coverage count, or -1 if crash/error.
 * ------------------------------------------------------------------------- */
static int run_seed(const char *seed_path) {
    memset(trace_bits, 0, MAP_SIZE); // Clear coverage

    pid_t pid = fork();
    if (pid < 0) {
        perror("fork");
        return -1;
    }

    if (pid == 0) {
        // Child process

        // Redirect the seed file -> stdin
        if (setup_stdio_file(seed_path) < 0) _exit(1);

        // Exec the target (already sees AFL_SHM_ID in environment).
        execv(target_argv[0], target_argv);

        // If execv fails
        perror("execv");
        _exit(1);
    } else {
        // Parent process
        int status = 0;
        waitpid(pid, &status, 0);

        if (WIFSIGNALED(status) || WEXITSTATUS(status) != 0) {
            // The target crashed or returned non-zero.
            return -1;
        }

        // Count coverage: number of non-zero bytes
        int coverage = 0;
        for (int i = 0; i < MAP_SIZE; i++) {
            if (trace_bits[i]) coverage++;
        }
        return coverage;
    }
}

/* -------------------------------------------------------------------------
 * mutate_seed: Minimal placeholder for AFL-like mutations (bit flip, etc.).
 * ------------------------------------------------------------------------- */
static size_t mutate_seed(const uint8_t *in_buf, size_t len,
                          uint8_t *out_buf, size_t max_len) {
    if (len > max_len) {
        fprintf(stderr, "mutate_seed: input too large (%zu > %zu)\n", len, max_len);
        return 0;
    }

    memcpy(out_buf, in_buf, len);
    size_t new_len = len;

    srand((unsigned) time(NULL));
    int strategy = rand() % 3;

    switch (strategy) {
        case 0: {
            // Flip a single bit
            if (new_len > 0) {
                int byte_pos = rand() % new_len;
                int bit_pos = rand() % 8;
                out_buf[byte_pos] ^= (1 << bit_pos);
            }
            break;
        }
        case 1: {
            // Increment a random byte
            if (new_len > 0) {
                int byte_pos = rand() % new_len;
                out_buf[byte_pos] += 1;
            }
            break;
        }
        case 2: {
            // "Havoc" style multiple changes
            int num_changes = (rand() % 5) + 1;
            for (int i = 0; i < num_changes; i++) {
                int byte_pos = rand() % new_len;
                out_buf[byte_pos] ^= (uint8_t) (rand() % 256);
            }
            break;
        }
    }

    return new_len;
}

/* -------------------------------------------------------------------------
 * main: usage: ./mini_fuzzer <target_binary> [args ...] <seed_file>
 * ------------------------------------------------------------------------- */
int main(int argc, char **argv) {
    if (argc < 3) {
        fprintf(stderr, "Usage: %s <instrumented_target> [args ...] <seed_file>\n", argv[0]);
        return 1;
    }

    // The seed file is the last argument.
    const char *seed_path = argv[argc - 1];

    // Everything between argv[1] and argv[argc-2] are target args, including the binary path.
    int target_argc = argc - 2; // exclude our own argv[0] and the seed file
    target_argv = calloc(target_argc + 1, sizeof(char *));
    if (!target_argv) {
        perror("calloc");
        return 1;
    }

    for (int i = 0; i < target_argc; i++) {
        target_argv[i] = argv[i + 1]; // shift over by 1
    }
    target_argv[target_argc] = NULL;

    // 1) Setup shared memory
    if (setup_shm() < 0) {
        fprintf(stderr, "Failed to setup shared memory.\n");
        free(target_argv);
        return 1;
    }

    // 2) Run the seed
    int coverage = run_seed(seed_path);
    if (coverage < 0) {
        fprintf(stderr, "[!] Target crashed or returned non-zero on '%s'\n", seed_path);
    } else {
        printf("[+] Coverage for original seed: %d\n", coverage);
    }

    // 3) Read the seed into a buffer
    FILE *f = fopen(seed_path, "rb");
    if (!f) {
        perror("fopen seed_path");
        remove_shm();
        free(target_argv);
        return 1;
    }

    fseek(f, 0, SEEK_END);
    long file_size = ftell(f);
    fseek(f, 0, SEEK_SET);

    if (file_size <= 0) {
        fprintf(stderr, "[!] Seed file is empty or unreadable.\n");
        fclose(f);
        remove_shm();
        free(target_argv);
        return 1;
    }

    uint8_t *seed_buf = malloc(file_size);
    if (!seed_buf) {
        perror("malloc seed_buf");
        fclose(f);
        remove_shm();
        free(target_argv);
        return 1;
    }

    fread(seed_buf, 1, file_size, f);
    fclose(f);

    // 4) Mutate the seed in memory
    uint8_t *mutated_buf = malloc(file_size * 2);
    if (!mutated_buf) {
        perror("malloc mutated_buf");
        free(seed_buf);
        remove_shm();
        free(target_argv);
        return 1;
    }
    size_t mutated_len = mutate_seed(seed_buf, file_size, mutated_buf, file_size * 2);

    // 5) Write mutated to a file, run coverage
    const char *mutated_file = "mutated_seed.dat";
    FILE *mf = fopen(mutated_file, "wb");
    if (!mf) {
        perror("fopen mutated_file");
        free(seed_buf);
        free(mutated_buf);
        remove_shm();
        free(target_argv);
        return 1;
    }
    fwrite(mutated_buf, 1, mutated_len, mf);
    fclose(mf);

    coverage = run_seed(mutated_file);
    if (coverage < 0) {
        fprintf(stderr, "[!] Target crashed or returned non-zero on mutated seed!\n");
    } else {
        printf("[+] Coverage for mutated seed: %d\n", coverage);
    }

    // Cleanup
    free(seed_buf);
    free(mutated_buf);
    remove_shm();
    free(target_argv);

    return 0;
}
