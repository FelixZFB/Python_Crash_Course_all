# -*- coding: cp936 -*-

#导入包
import matplotlib.pyplot as plt
import numpy as np
#支持中文显示
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
 
#创建数据
x = np.linspace(-5, 5, 100)
y1 = np.sin(x)
y2 = np.cos(x)
 
#创建figure窗口
plt.figure(num=3, figsize=(8, 5))
#画曲线1
plt.plot(x, y1)
#画曲线2
plt.plot(x, y2, color='blue', linewidth=5.0, linestyle='--')
#设置坐标轴范围
plt.xlim((-5, 5))
plt.ylim((-2, 2))
#设置坐标轴名称
plt.xlabel('xxxxxxxxxxx')
plt.ylabel('yyyyyyyyyyy')
#设置坐标轴刻度
my_x_ticks = np.arange(-5, 5, 0.5)
my_y_ticks = np.arange(-2, 2, 0.3)
plt.xticks(my_x_ticks)
plt.yticks(my_y_ticks)
 
#显示出所有设置
plt.show()
