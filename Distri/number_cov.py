import pandas as pd
import matplotlib.pyplot as plt

def plot_coverage_trend(csv_path, save_path, title="Coverage Comparison Over Samples"):
    df = pd.read_csv(csv_path)

    plt.figure(figsize=(10, 6))

    for col in df.columns[1:]:  # 跳过第一列 Sample Count
        plt.plot(df[df.columns[0]], df[col], marker='o', label=col)

    plt.xlabel("Number of Samples")
    plt.ylabel("Coverage (e.g., paths_total)")
    plt.title(title)
    plt.grid(True)
    plt.legend()
    plt.xticks(df[df.columns[0]])
    plt.tight_layout()
    plt.savefig(save_path)
    # plt.show()

# 示例调用
plot_coverage_trend(
    "sample_coverage.csv",
    "img/coverage_comparison.png",
    title="Coverage Trend of Different Fuzzers"
)
