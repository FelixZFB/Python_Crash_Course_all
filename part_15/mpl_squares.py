# -*- coding: cp936 -*-
# 绘制简单的折线图
# 当给plot提供数据时，默认数据第一个值对应的x坐标为0，所以画出的图形1对应的x为0
# 25对应的x为4，修正方法1，第一个值给0
# 修正方法2，同时给定输入值和输出值

import matplotlib.pyplot as plt

squares = [1, 4, 9 , 16, 25]
plt.plot(squares, linewidth=5)

# 设置图表标题，并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)

plt.show()


# 修正方法1

squares = [0, 1, 4, 9 , 16, 25]
plt.plot(squares, linewidth=5)

# 设置图表标题，并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)

plt.show()


# 修正方法2

input_values = [1, 2, 3, 4 , 5]
squares = [1, 4, 9 , 16, 25]
plt.plot(input_values, squares, linewidth=5)

# 设置图表标题，并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)

plt.show()



