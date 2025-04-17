import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def plot_multiple_afl_paths(data_list, save_path, title):
    """
    data_list: List of tuples (plot_data_path, label, color)
    save_path: Output image file path
    """
    plt.figure(figsize=(10, 5))
    max_time = 0  # 用于确定 X 轴范围

    for path, label, color in data_list:
        raw_data = []
        with open(path, 'r') as f:
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

        # 数据类型转换
        df["unix_time"] = df["unix_time"].astype(int)
        df["paths_total"] = df["paths_total"].astype(int)
        df["minutes_elapsed"] = (df["unix_time"] - df["unix_time"].iloc[0]) / 60.0

        # 绘图
        plt.plot(df["minutes_elapsed"], df["paths_total"],
                 marker='o', label=label, color=color)

        max_time = max(max_time, df["minutes_elapsed"].max())
        print(f"[+] Plotted: {label} ({len(df)} points)")

    # 图形美化
    plt.xlabel("Elapsed Time (minutes)")
    plt.ylabel("Paths Total")
    plt.title(title)
    plt.grid(True)
    plt.legend()

    # 设置横轴刻度（每 60 分钟一个）
    xticks = np.arange(0, max_time + 1, 60)
    plt.xticks(xticks, rotation=45)

    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()
    print(f"[✓] Plot saved to: {save_path}")

# 示例用法
if __name__ == "__main__":
    plot_multiple_afl_paths([
        ("/home/out-superion/jsc-24/1/plot_data", "Superion-JSC", "tab:blue"),
        ("/home/out-distri/jsc/2/plot_data", "Distri-JSC", "tab:orange")
    ], "compare_paths_jsc.png",
    "JSC: Paths Over Time"
    )
    plot_multiple_afl_paths([
        ("/home/out-superion/jerry-24/1/plot_data", "Superion-Jerry", "tab:blue"),
        ("/home/out-distri/jerry/1/plot_data", "Distri-Jerry", "tab:orange")
    ], "compare_paths_je.png",
    "Jerry: Paths Over Time"
    )
