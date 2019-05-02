# -*- coding: cp936 -*-
# 详细见P297
# 随机漫步,可视化
# 绘制路径图和散点图，模拟分子运动

import matplotlib.pyplot as plt
from random_walk import RandomWalk

# 只要程序处于活动状态，就不断的模拟随机漫步
while True:
    # 创建一个RandomWalk的实例，执行获取300个随机的点的方法
    rw = RandomWalk(300)
    rw.fill_walk()
    
    # 设置绘图窗口的尺寸
    plt.figure(figsize=(10, 6))
    
    # 绘制路径图,点标记为+，线条点划线-.
    plt.plot(rw.x_values, rw.y_values, linestyle='-.', linewidth=1, c='b', marker='+')
    
    # 突出起点和终点，绘制两个散点
    plt.scatter(0,0, c='red', edgecolor='none', s=300)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='yellow', 
            edgecolor='none', s=300)
            
    # 隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    
    plt.show()

    # 添加一个结束语句
    keep_running = input("Make another walk? (Y/N): ")
    if keep_running == 'N':
        break


            

