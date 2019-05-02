# -*- coding: cp936 -*-
# 详细见P305
# 投掷骰子,出现的频率，发现某些数字出现的最多，
# 因为两个筛子就存在某些组合的问题，求和为7的组合最多

import pygal
from die import Die

# 创建两个个D6实例
die_1 = Die()
die_2 = Die()

# 投掷几次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(1000):
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

# 对结果进行可视化,设置一个绘图实例
hist = pygal.Bar()
# 设置标题
hist.title = "Results of rolling one D6 1000 times."
# 提取X轴的值
hist.x_labels = []
for x in range(2, 13):
    hist.x_labels.append(x)
print(hist.x_labels)
# 设置X坐标名称
hist.x_title = "Result"
# 设置Y轴标题
hist.y_title = "Frequency of Result"
# 添加Y轴数据及说明
hist.add('D6 + D6', frequencies)
# 输出矢量图形，采用浏览器打开
hist.render_to_file('die_visual_1.svg')



            

