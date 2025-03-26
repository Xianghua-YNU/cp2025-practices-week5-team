import numpy as np
import matplotlib.pyplot as plt


def random_walk_finals(num_steps=1000, num_walks=1000):
    """生成多个二维随机游走的终点位置

    通过模拟多次随机游走，每次在x和y方向上随机选择±1移动，
    计算所有随机游走的终点坐标。

    参数:
        num_steps (int, optional): 每次随机游走的步数. 默认值为1000
        num_walks (int, optional): 随机游走的次数. 默认值为1000

    返回:
        tuple: 包含两个numpy数组的元组 (x_finals, y_finals)
            - x_finals: 所有随机游走终点的x坐标数组
            - y_finals: 所有随机游走终点的y坐标数组
    """
    # TODO: 实现随机游走算法
    # 提示：
    # 1. 使用np.zeros初始化数组
    # 2. 使用np.random.choice生成随机步长
    # 3. 使用np.sum计算总位移
    x_steps = np.random.choice([-1,1], size=(num_walks, num_steps))  #生成x y方向上的步长矩阵，每个元素独立取+-1
    y_steps = np.random.choice([-1,1], size=(num_walks, num_steps))  #形状 :(num_walks,num_steps)每行代表一次独立游走
    x_finals = np.sum(x_steps, axis=1)  #计算每个游走的累积位移，即每行的累加和（沿axis=1求和）
    y_finals = np.sum(y_steps, axis=1)
    return x_finals, y_finals



def calculate_mean_square_displacement():
    """计算不同步数下的均方位移

    对于预设的步数序列[1000, 2000, 3000, 4000]，分别进行多次随机游走模拟，
    计算每种步数下的均方位移。每次模拟默认进行1000次随机游走取平均。

    返回:
        tuple: 包含两个numpy数组的元组 (steps, msd)
            - steps: 步数数组 [1000, 2000, 3000, 4000]
            - msd: 对应的均方位移数组
    """
    # TODO: 实现均方位移计算
    # 提示：
    # 1. 使用random_walk_finals获取终点坐标
    # 2. 计算位移平方和
    # 3. 使用np.mean计算平均值
    steps = np.array([1000, 2000, 3000, 4000])  #预设的步数序列
    msd = np.zeros(len(steps))  #初始化MSD储存数组
    for i, n in enumerate(steps):
        x,y =random_walk_finals(num_steps=n,num_walks=1000) #进行1000次随机游走，获取终点坐标
        displacement_sq = x**2+y**2  #计算每个游走的位移平方和
        msd[i] = np.mean(displacement_sq)  #计算均方位移（取平均值）
    return steps, msd





def analyze_step_dependence():
    """分析均方位移与步数的关系，并进行最小二乘拟合

    返回:
        tuple: (steps, msd, k)
            - steps: 步数数组
            - msd: 对应的均方位移数组
            - k: 拟合得到的比例系数
    """
    # TODO: 实现数据分析
    # 提示：
    # 1. 调用calculate_mean_square_displacement获取数据
    # 2. 使用最小二乘法拟合 msd = k * steps
    # 3. k = Σ(N·msd)/Σ(N²)
    steps,msd = calculate_mean_square_displacement()  #获取不同步数下的均方位移数据
    numerator = np.sum(steps*msd)  #最小二乘法拟合msd=k*steps
    denominator = np.sum(steps**2)  #计算分子和分母
    k = numerator/denominator  #计算比例系数k
    return steps, msd, k




if __name__ == "__main__":
    # TODO: 完成主程序
    # 提示：
    # 1. 获取数据和拟合结果
    # 2. 绘制实验数据点和理论曲线
    # 3. 设置图形属性
    # 4. 打印数据分析结果
    steps, msd, k = analyze_step_dependence()  #获取数据和拟合结果
    plt.figure(figsize=[10,6])  #创建绘图窗口
    plt.scatter(steps, msd,s=100,edgecolor='black', label=f'Simulation Data({len(steps)}point',zorder=3)  #绘制实验数据点
    fit_line = k*steps
    plt.plot(steps, fit_line, 'r--',lw=2,label=f'Linear Fit:MSD={k:.3f}N',zorder=2)     #绘制理论拟合线
    plt.plot(steps,2*steps,'g-',lw=2,label='Theoretical:MSD=2N',zorder=1)  #绘制理论曲线（拟合曲线）
    plt.title('均方位移与步数的关系',fontsize=14)  #设置图形属性
    plt.xlabel('步数(N)', fontsize=12)
    plt.ylabel('均方位移(MSD)', fontsize=12)
    plt.legend()
    plt.grid(True,alpha=0.3)
    plt.tight_layout()
    plt.show()  #显示图形
    print("数据分析结果:")  #打印数据分析结果
    print(f"步数:{steps}")
    print(f"均方位移:{msd}")
    print(f"拟合得到的比例系数k:{k:.4f}")
    print("理论预期值k=2.0（二维无约束随机游走）",f"相对误差:{abs(k-2.0)/2.0*100:.2f}%")
