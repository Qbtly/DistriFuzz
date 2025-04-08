import matplotlib.pyplot as plt
import csv
from datetime import datetime

def plot_fitness_over_time(log_file='/home/qq/DistriFuzz/fitness_log(mmd).csv'):
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

    # 绘图
    plt.figure(figsize=(10, 5))
    plt.plot(timestamps, fitness_values, marker='o', linestyle='-')
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
