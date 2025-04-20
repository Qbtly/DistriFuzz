import matplotlib.pyplot as plt
import csv
import numpy as np
import pandas as pd

def plot_trend_comparison(fitness_log, plot_data_file, save_path, title):
    # === 读取 fitness_log.csv ===
    timestamps = []
    fitness_values = []

    with open(fitness_log, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) < 3:
                continue
            ts = int(row[0])
            fitness = float(row[2])
            timestamps.append(ts)
            fitness_values.append(fitness)

    if not timestamps:
        print("No fitness data.")
        return

    start_time = timestamps[0]
    elapsed_minutes_fitness = [(t - start_time) / 60.0 for t in timestamps]

    # === 读取 AFL 的 plot_data ===
    raw_data = []
    with open(plot_data_file, 'r') as f:
        for line in f:
            if line.startswith("#") or not line.strip():
                continue
            fields = [x.strip().rstrip('%') for x in line.strip().split(',')]
            raw_data.append(fields)

    df = pd.DataFrame(raw_data, columns=[
        "unix_time", "cycles_done", "cur_path", "paths_total",
        "pending_total", "pending_favs", "map_size", "unique_crashes",
        "unique_hangs", "max_depth", "execs_per_sec"
    ])
    df["unix_time"] = df["unix_time"].astype(int)
    df["paths_total"] = df["paths_total"].astype(int)
    df["minutes_elapsed"] = (df["unix_time"] - df["unix_time"].iloc[0]) / 60.0

    # === 绘图：双 Y 轴 ===
    fig, ax1 = plt.subplots(figsize=(12, 6))

    # 曲线 1：fitness
    ax1.plot(elapsed_minutes_fitness, fitness_values, color='tab:blue', label="Fitness", marker='o')
    ax1.set_xlabel("Elapsed Time (minutes)")
    ax1.set_ylabel("Fitness", color='tab:blue')
    ax1.tick_params(axis='y', labelcolor='tab:blue')

    # 曲线 2：paths_total
    ax2 = ax1.twinx()
    ax2.plot(df["minutes_elapsed"], df["paths_total"], color='tab:orange', label="Paths Total", marker='x')
    ax2.set_ylabel("Paths Total", color='tab:orange')
    ax2.tick_params(axis='y', labelcolor='tab:orange')

    # 公共设置
    plt.title(title)
    ax1.grid(True)

    # 添加图例（合并 ax1 + ax2 的图例）
    lines_1, labels_1 = ax1.get_legend_handles_labels()
    lines_2, labels_2 = ax2.get_legend_handles_labels()
    plt.legend(lines_1 + lines_2, labels_1 + labels_2, loc='upper left')

    # X轴时间刻度
    max_time = max(max(elapsed_minutes_fitness), df["minutes_elapsed"].max())
    xticks = np.arange(0, max_time + 1, 60)
    plt.xticks(xticks, rotation=45)


    fig.tight_layout()
    plt.savefig(save_path)
    plt.show()

plot_trend_comparison(
    "/home/DistriFuzz/Distri/logs/fitness_jerry_test3.csv",
    "/home/out-distri/jerry-test/3/plot_data",
    "fp_jerry_test3.png",
    "Jerry: Fitness vs AFL Paths Over Time"
)
print('fp_jerry_test3.png saved!')
# plot_trend_comparison(
#     "/home/DistriFuzz/Distri/logs/fitness_jerry2.csv",
#     "/home/out-distri/jerry/2/plot_data",
#     "fp_jerry2.png",
#     "Jerry: Fitness vs AFL Paths Over Time"
# )
# plot_trend_comparison(
#     "/home/DistriFuzz/Distri/logs/fitness_jsc2.csv",
#     "/home/out-distri/jsc/2/plot_data",
#     "fp_jsc2.png",
#     "JSC: Fitness vs AFL Paths Over Time"
# )
# plot_trend_comparison(
#     "/home/DistriFuzz/Distri/logs/fitness_jerry3.csv",
#     "/home/out-distri/jerry/3/plot_data",
#     "fp_jerry3.png",
#     "Jerry: Fitness vs AFL Paths Over Time"
# )
# plot_trend_comparison(
#     "/home/DistriFuzz/Distri/logs/fitness_jsc3.csv",
#     "/home/out-distri/jsc/3/plot_data",
#     "fp_jsc3.png",
#     "JSC: Fitness vs AFL Paths Over Time"
# )