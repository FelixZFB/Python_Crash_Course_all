# -*- coding: cp936 -*-
# 详细见P305
# 投掷骰子，统计每一面出现的频率，柱状图可视化

import pygal
from die import Die

# 创建一个D6实例
die = Die()

# 投掷几次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# 分析结果各个数字出现的评率
frequencies = []
for value in range(1, die.num_sides+1):
    # count函数可以统计一个值在列表中出现的次数
    frequency = results.count(value)
    frequencies.append(frequency)
# 打印出每一面出现的次数
print(['1', '2', '3', '4', '5', '6'])
print(frequencies)

# 对结果进行可视化，绘制柱形图
hist = pygal.Bar()

# 设置标题
hist.title = "Results of rolling one D6 1000 times."
# 设置X坐标名称
hist.x_labels = ['1', '2', '3', '4', '5', '6']
# 设置X轴标题
hist.x_title = "Result"
# 设置Y轴标题
hist.y_title = "Frequency of Result"
# 添加Y轴数据及说明
hist.add('D6', frequencies)
# 输出矢量图形，采用浏览器打开
hist.render_to_file('die_visual.svg')



            

