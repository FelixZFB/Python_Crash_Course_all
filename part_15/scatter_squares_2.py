# -*- coding: cp936 -*-
# 绘制一系列点的散点图，自动计算数据
# 详细见P292

import matplotlib.pyplot as plt

# 绘制多个点

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, c='blue', edgecolor='yellow', s=30)

# 设置图表标题并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', which='both', colors='blue', labelsize=14)

# 设置每个坐标轴的取值范围
plt.axis([0, 50, 0, 2500])

plt.show()

