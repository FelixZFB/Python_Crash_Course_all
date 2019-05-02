# -*- coding: cp936 -*-
# 详细见P309
# 投掷两个不同面的骰子，采用matplotlib.pyplot绘制柱形图

import matplotlib.pyplot as plt
from die import Die

# 创建一个D6和一个D6实例
die_1 = Die()
die_2 = Die()

# 投掷几次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(500):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# 分析结果各个数字出现的评率
frequencies = []
max_result = die_1.num_sides + die_2.num_sides 
for value in range(2, max_result+1):
    # count函数可以统计一个值在列表中出现的次数
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)
print(list(range(2, 13)))

# 对结果进行可视化,使用matplotlib绘制柱形图
x_labels = list(range(2, 13))
plt.bar(range(2, 13), frequencies, color='rgb', tick_label=range(2, 13))
plt.show()


            

