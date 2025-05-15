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
    plt.xlim(0, 400)
    plt.ylim(0, 7000)
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
        "/home/out-superion/jsc-24/1/plot_data",
        "/home/out-superion/jsc-afl/1/plot_data",
        # "/home/out-superion/jsc-24/2/plot_data",
        "/home/out-distri/nm/jsc/5/plot_data",
        "/home/out-distri/n/jsc/5/plot_data",
        # "/home/out-distri/m/jsc/5/plot_data",
        # "/home/out-distri/mn/jsc/5/plot_data",
        # "/home/out-distri/n/jsc/51/plot_data",
        # "/home/out-distri/n/jsc/52/plot_data",
        # "/home/out-distri/n/jsc/53/plot_data",
        "/home/out-distri/n/jsc53/53/plot_data",
        
        # "/home/out-distri/nm/jsc/52/plot_data",
        # "/home/out-distri/nm/jsc/53/plot_data",
        "/home/out-distri/nm/jsc54/54/plot_data",
        # "/home/out-distri/i/jsc/5/plot_data",
    ],
    labels=[
        "JSC superion 1",
        "JSC AFL 1",
        "JSC 0.7novel 0.3mmd 5",
        "JSC 1novel 5",
        # "JSC 1mmd 5",
        # "JSC 0.7mmd 0.3novel 5",
        # "JSC 1novel 51",
        # "JSC 1novel 52 bitflip",
        # "JSC 1novel 53 AFL wrong",
        "JSC 1novel 53 AFL",
        # "JSC 0.7novel 0.3mmd 52 wrong",
        # "JSC 0.7novel 0.3mmd 53 AFL wrong",
        "JSC 0.7novel 0.3mmd 54 AFL",
        # "JSC interest 51",
    ],
    save_path="img/p_jsc_compare5.png",
    title="JSC Engine: AFL Path Growth Comparison"
)

compare_multiple_plot_data(
    plot_data_files=[
        "/home/out-distri/nm/jerry/5/plot_data",
        "/home/out-distri/n/jerry/5/plot_data",
        "/home/out-distri/m/jerry/5/plot_data",
        "/home/out-distri/mn/jerry/5/plot_data",
        
    ],
    labels=[
        "Jerry 0.7novel 0.3mmd 5",
        "Jerry 1novel 5",
        "Jerry 0.7mmd 0.3novel 5",
        "Jerry 1mmd 5",
    ],
    save_path="img/p_jerry_compare5.png",
    title="JSC Engine: AFL Path Growth Comparison"
)