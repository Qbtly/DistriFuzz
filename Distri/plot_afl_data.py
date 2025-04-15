import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

def plot_afl_plot_data(file_path):
    raw_data = []
    
    with open(file_path, 'r') as f:
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

    # 类型转换
    df["unix_time"] = df["unix_time"].astype(int)
    df["paths_total"] = df["paths_total"].astype(int)
    df["map_size"] = df["map_size"].astype(float)

    # 计算运行时间（相对时间）
    start_time = df["unix_time"].iloc[0]
    df["minutes_elapsed"] = (df["unix_time"] - start_time) / 60.0

    # 绘图
    plt.figure(figsize=(10, 5))
    plt.plot(df["minutes_elapsed"], df["paths_total"], marker='o', label="Paths Total")
    # 若想加覆盖率：
    # plt.plot(df["minutes_elapsed"], df["map_size"], marker='x', label="Coverage %")

    plt.xlabel("Elapsed Time (minutes)")
    plt.ylabel("Value")
    plt.title("AFL Fuzzing Trend (Paths over Time)")
    plt.grid(True)
    plt.legend()

     # 设置横轴刻度为每 20 分钟一个
    import numpy as np
    max_time = df["minutes_elapsed"].max()
    xticks = np.arange(0, max_time + 1, 60)
    plt.xticks(xticks, rotation=45)

    plt.tight_layout()
    plt.savefig("afl_plot_data_trend.png")
    plt.show()

# 用法示例
if __name__ == "__main__":
    plot_afl_plot_data("/home/out-superion/jsc-24/1/plot_data")
