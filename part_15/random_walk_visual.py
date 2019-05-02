# -*- coding: cp936 -*-
# 详细见P297
# 随机漫步,可视化
# 绘制散点图

import matplotlib.pyplot as plt
from random_walk import RandomWalk

# 只要程序处于活动状态，就不断的模拟随机漫步
while True:
    # 创建一个RandomWalk的实例
    rw = RandomWalk(10000)
    rw.fill_walk()
    
    # 设置绘图窗口的尺寸
    plt.figure(figsize=(10, 6))
    
    # 绘制散点图，设置颜色映射，边缘色，透明度，尺寸
    plt.scatter(rw.x_values, rw.y_values, c=rw.x_values, 
            cmap=plt.cm.plasma, edgecolor='none', alpha=0.3, s=5)
    
    # 突出起点和终点
    plt.scatter(0,0, c='green', edgecolor='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', 
            edgecolor='none', s=100)
            
    # 隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    
    plt.show()
    
    # 添加一个break结束语句
    keep_running = input("Make another walk? (Y/N): ")
    if keep_running == 'N':
        break


            

