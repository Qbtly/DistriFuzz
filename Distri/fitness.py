import matplotlib.pyplot as plt
import csv
import numpy as np

def plot_fitness_over_time(log_file='/home/DistriFuzz/fitness_log(mmd).csv'):
    timestamps = []
    fitness_values = []

    # 读取 CSV 文件
    with open(log_file, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) < 3:
                continue
            ts = int(row[0])
            fitness = float(row[2])
            timestamps.append(ts)
            fitness_values.append(fitness)

    if not timestamps:
        print("No data found.")
        return

    # 转换为运行时间（分钟）
    start_time = timestamps[0]
    elapsed_minutes = [(t - start_time) / 60.0 for t in timestamps]

    # 控制稀疏程度
    step = 30
    sparse_elapsed = elapsed_minutes[::step]
    sparse_fitness = fitness_values[::step]

    # 绘图
    plt.figure(figsize=(12, 6))
    plt.plot(sparse_elapsed, sparse_fitness, marker='o', linestyle='-')

    # 标注前/后 N 个点
    N = 5
    for i, (x, y) in enumerate(zip(sparse_elapsed, sparse_fitness)):
        if i < N or i >= len(sparse_fitness) - N:
            plt.text(x, y + 0.2, f"{y:.2f}", ha='center', fontsize=8)

    plt.xlabel("Elapsed Time (minutes)")
    plt.ylabel("Max Fitness")
    plt.title("Fitness over Time")
    plt.grid(True)

    # 设置横轴刻度为每 20 分钟一个
    max_time = max(sparse_elapsed)
    xticks = np.arange(0, max_time + 1, 60)
    plt.xticks(xticks, rotation=45)

    plt.tight_layout()
    plt.savefig("fitness_trend(mmd).png")
    print("图已保存为 fitness_trend(mmd).png")

plot_fitness_over_time()
