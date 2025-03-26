import numpy as np
import matplotlib.pyplot as plt

def generate_coin_sequence(n_flips, p_head=0.08):
    """生成硬币序列，1表示正面，0表示反面"""
    return np.random.choice([0, 1], size=n_flips, p=[1-p_head, p_head])

def calculate_waiting_times(coin_sequence):
    """计算两次正面之间的等待时间（反面次数）"""
    # 找到所有正面（值为1）的位置索引
    head_indices = np.nonzero(coin_sequence)[0]

    # 计算连续两个正面之间的间隔（差值-1得到中间的反面数量）
    waiting_times = np.diff(head_indices) - 1
    return waiting_times

def plot_waiting_time_histogram(waiting_times, log_scale=False, n_flips=None):
    """绘制等待时间直方图"""
    plt.figure(figsize=(10, 6))
    
    # 确定合适的bin数量
    max_wait = max(waiting_times) if len(waiting_times) > 0 else 0
    bins = np.arange(0, max_wait + 2) - 0.5  # 确保每个整数值有一个bin
    
    # 绘制直方图
    plt.hist(waiting_times, bins=bins, density=True, alpha=0.7)
    plt.xlabel('Waiting Time (Number of Tails)')
    plt.ylabel('Frequency' if not log_scale else 'Frequency (Log Scale)')
    
    # 设置y轴为对数刻度（如果需要）
    if log_scale:
        plt.yscale('log')
        title = 'Waiting Time Distribution (Semi-log Scale)'
    else:
        title = 'Waiting Time Distribution'
    
    # 在标题中添加抛硬币次数
    if n_flips is not None:
        title += f' - {n_flips:,} Coin Flips'
    
    plt.title(title)
    plt.grid(True, alpha=0.3)
    plt.show()

def analyze_waiting_time(waiting_times):
    """分析等待时间的统计特性"""
    if len(waiting_times) == 0:
        return {"mean": None, "std": None, "theoretical_mean": None}
    
    mean_wait = np.mean(waiting_times)
    std_wait = np.std(waiting_times)
    
    # 理论上，等待时间应该服从几何分布，均值为(1-p)/p
    p_head = 0.08  # 硬币正面概率
    theoretical_mean = (1 - p_head) / p_head
    
    # 如果考虑指数分布模型（泊松过程中的等待时间）
    exponential_mean = 1 / p_head  # 1/λ = 1/0.08 = 12.5
    
    return {
        "mean": mean_wait,
        "std": std_wait,
        "theoretical_mean": theoretical_mean,
        "exponential_mean": exponential_mean
    }

def run_experiment(n_flips, title):
    """运行一次等待时间实验
    
    参数:
        n_flips: 抛硬币次数
        title: 实验标题
    """
    print(f"===== {title} =====")
    
    # 生成硬币序列并计算等待时间
    coin_sequence = generate_coin_sequence(n_flips)
    waiting_times = calculate_waiting_times(coin_sequence)
    
    # 分析等待时间
    stats = analyze_waiting_time(waiting_times)
    print(f"Average waiting time: {stats['mean']:.2f}")
    print(f"Theoretical average waiting time (Geometric): {stats['theoretical_mean']:.2f}")
    print(f"Theoretical average waiting time (Exponential): {stats['exponential_mean']:.2f}")
    
    # 绘制直方图
    plot_waiting_time_histogram(waiting_times, log_scale=False, n_flips=n_flips)
    plot_waiting_time_histogram(waiting_times, log_scale=True, n_flips=n_flips)
    
    return waiting_times, stats

if __name__ == "__main__":
    # 设置随机种子以保证可重复性
    np.random.seed(42)
    
    # 任务一：1000次抛掷
    waiting_times_1k, stats_1k = run_experiment(1000, "Task 1: 1000 Coin Flips")
    
    # 任务二：1000000次抛掷
    print("\n")
    waiting_times_1m, stats_1m = run_experiment(1000000, "Task 2: 1,000,000 Coin Flips")
    waiting_times_1m, stats_1m = run_experiment(1000000, "Task 2: 1,000,000 Coin Flips")
