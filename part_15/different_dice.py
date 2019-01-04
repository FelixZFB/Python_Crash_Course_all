# -*- coding: cp936 -*-
# 详细见P309
# 投掷两个不同面的骰子

import pygal
from die import Die

# 创建一个D6和一个D10实例
die_1 = Die()
die_2 = Die(10)

# 投掷几次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)
    
# print(results)

# 分析结果各个数字出现的评率
frequencies = []
max_result = die_1.num_sides + die_2.num_sides 
for value in range(2, max_result+1):
    # count函数可以统计一个值在列表中出现的次数
    frequency = results.count(value)
    frequencies.append(frequency)
    
print(frequencies)

# 对结果进行可视化

hist = pygal.Bar()

hist.title = "Results of rolling a D6 and a D10 50,000 times."

hist.x_labels = []
for x in range(2, 17):
    hist.x_labels.append(x)
print(hist.x_labels)

hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D10', frequencies)
hist.render_to_file('different_dice.svg')



            

