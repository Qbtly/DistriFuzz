import matplotlib.pyplot as plt
import re

def parse_afl_cov_log(file_path):
    timestamps = []
    lines_cov = []
    funcs_cov = []
    branches_cov = []

    with open(file_path, 'r') as f:
        step = 0
        for line in f:
            line = line.strip()

            match = re.match(r"lines\.+:\s+([\d\.]+)%.*", line)
            if match:
                lines_cov.append(float(match.group(1)))
                timestamps.append(step)
                step += 1
                continue

            match = re.match(r"functions\.+:\s+([\d\.]+)%.*", line)
            if match:
                funcs_cov.append(float(match.group(1)))
                continue

            match = re.match(r"branches\.+:\s+([\d\.]+)%.*", line)
            if match:
                branches_cov.append(float(match.group(1)))
                continue

    return timestamps, lines_cov, funcs_cov, branches_cov

def plot_coverage_trend(log_file='coverage.log'):
    x, lines, funcs, branches = parse_afl_cov_log(log_file)

    plt.figure(figsize=(12, 6))

    def plot_with_labels(x, y, label, marker):
        plt.plot(x, y, label=label, marker=marker)
        for i, (x_i, y_i) in enumerate(zip(x, y)):
            plt.text(x_i, y_i + 0.5, f"{y_i:.1f}%", ha='center', va='bottom', fontsize=8)

    plot_with_labels(x, lines, 'Line Coverage', 'o')
    plot_with_labels(x, funcs, 'Function Coverage', 's')
    plot_with_labels(x, branches, 'Branch Coverage', '^')

    plt.xlabel("Step")
    plt.ylabel("Coverage (%)")
    plt.title("AFL Coverage Trend with Value Labels")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("afl_coverage_trend_annotated.png")
    print("图已保存为 afl_coverage_trend_annotated.png")

# 使用示例
plot_coverage_trend("/home/qq/out/1/cov/afl-cov.log")
