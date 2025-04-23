import matplotlib.pyplot as plt
import numpy as np

def random_walk_2d(steps):
    """生成二维随机行走轨迹
    
    参数:
        steps (int): 随机行走的步数
        
    返回:
        tuple: 包含x和y坐标序列的元组 (x_coords, y_coords)
    """
    # TODO: 实现随机行走算法
    # 提示：
    # 1. 使用 np.random.choice 生成随机步长 ([-1, 1])
    # 2. 分别生成x和y方向的步长序列
    # 3. 使用 cumsum() 计算累积和得到轨迹
    x_step = np.random.choice([-1,1],steps)
    y_step = np.random.choice([-1,1],steps)
    x_trace = np.cumsum(x_step)
    y_trace = np.cumsum(y_step)
    return (x_trace, y_trace)

def plot_single_walk(path):
    """绘制单个随机行走轨迹
    
    参数:
        path (tuple): 包含x和y坐标序列的元组
    """
    # TODO: 实现单个轨迹的绘制
    # 提示：
    # 1. 使用 plt.plot 绘制轨迹线
    # 2. 使用 plt.scatter 标记起点和终点
    # 3. 设置坐标轴比例相等
    # 4. 添加图例
    x = path[0]
    y = path[1]
    plt.plot(x,y)
    plt.scatter(0,0,s=100,c= 'b',label='start')
    plt.scatter(x[-1],y[-1],s=100,c= 'r',label='end')
    plt.legend()
    plt.axis('equal')
    

def plot_multiple_walks():
    """在2x2子图中绘制四个不同的随机行走轨迹"""
    # TODO: 实现多个轨迹的绘制
    # 提示：
    # 1. 创建2x2的子图布局
    # 2. 对每个子图重复以下步骤：
    #    - 生成随机行走轨迹
    #    - 绘制轨迹线
    #    - 标记起点和终点
    #    - 设置标题和图例
    fig,axes = plt.subplots(2,2,layout='constrained')
    axes = axes.ravel()#将axes矩阵拉成一维
    for i in range(4):
        path = random_walk_2d(1000)
        
        
        x,y = path
        axes[i].plot(x,y)
        axes[i].scatter(0,0,s=100,c= 'b',label='start')
        axes[i].scatter(x[-1],y[-1],s=100,c= 'r',label='end')
        axes[i].axis('equal')
        axes[i].legend()
        axes[i].set_title(f'Trajectory {i+1}')
    

if __name__ == "__main__":
    # TODO: 完成主程序逻辑
    # 1. 生成并绘制单个轨迹
    # 2. 生成并绘制多个轨迹
    PATH = random_walk_2d(1000)
    
    plot_single_walk(PATH)
    plt.show()
    plot_multiple_walks()
    plt.show()
