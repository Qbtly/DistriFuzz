import matplotlib.pyplot as plt
import csv
from datetime import datetime

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
            timestamps.append(datetime.fromtimestamp(ts))  # 转为人类可读时间
            fitness_values.append(fitness)

    # 控制稀疏程度
    step = 30
    sparse_timestamps = timestamps[::step]
    sparse_fitness = fitness_values[::step]

    # 绘图
    plt.figure(figsize=(12, 6))
    plt.plot(sparse_timestamps, sparse_fitness, marker='o', linestyle='-')

    N = 5
    for i, (x, y) in enumerate(zip(sparse_timestamps, sparse_fitness)):
        if i < N or i >= len(sparse_fitness) - N:
            plt.text(x, y + 0.2, f"{y:.2f}", ha='center', fontsize=8)


    plt.xlabel("Time")
    plt.ylabel("Max Fitness")
    plt.title("Fitness over Time")
    plt.grid(True)
    plt.tight_layout()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("fitness_trend(mmd).png")
    print("图已保存为 fitness_trend.png")


plot_fitness_over_time()
