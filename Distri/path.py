import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def compare_multiple_plot_data(plot_data_files, labels, save_path, title):
    assert len(plot_data_files) == len(labels), "File list and label list must be the same length."

    plt.figure(figsize=(12, 6))

    for file_path, label in zip(plot_data_files, labels):
        raw_data = []
        with open(file_path, 'r') as f:
            for line in f:
                if line.startswith("#") or not line.strip():
                    continue
                fields = [x.strip().rstrip('%') for x in line.strip().split(',')]
                raw_data.append(fields)

        if not raw_data:
            print(f"[WARN] File {file_path} has no valid data.")
            continue

        df = pd.DataFrame(raw_data, columns=[
            "unix_time", "cycles_done", "cur_path", "paths_total",
            "pending_total", "pending_favs", "map_size", "unique_crashes",
            "unique_hangs", "max_depth", "execs_per_sec"
        ])
        df["unix_time"] = df["unix_time"].astype(int)
        df["paths_total"] = df["paths_total"].astype(int)
        df["minutes_elapsed"] = (df["unix_time"] - df["unix_time"].iloc[0]) / 60.0

        plt.plot(df["minutes_elapsed"], df["paths_total"], label=label, marker='o')

    plt.xlabel("Elapsed Time (minutes)")
    plt.ylabel("Paths Total")
    plt.title(title)
    plt.grid(True)
    plt.legend(loc='upper left')
    plt.tight_layout()
    plt.savefig(save_path)
    # plt.show()


compare_multiple_plot_data(
    plot_data_files=[
        "/home/out-distri/jsc-test/4/plot_data",
        "/home/out-distri/jsc-test/5/plot_data",
        "/home/out-distri/jsc-test/7/plot_data"
    ],
    labels=[
        "Jerry Test 4",
        "Jerry Test 5",
        "Jerry Test 7"
    ],
    save_path="p_jsc_compare.png",
    title="JSC Engine: AFL Path Growth Comparison"
)
