# -*- coding: cp936 -*-
# 详细见P322
# 分析CSV文件,获取日期，最高气温，最低气温
# 处理存在异常数据的文件，存在空字符串的文件

import csv
import numpy as np
from datetime import datetime
from matplotlib import pyplot as plt


filename = 'death_valley_2014.csv'
with open(filename) as f:
    
    # 读取整个文件的内容
    reader = csv.reader(f)
    
    # 读取文件的第一行内容
    header_row = next(reader)

    # 打印文件头及其位置，索引是第几列，及其对应的内容


    # 上面输出显示获取文件中的最高气温，上面输出显示，第0列为日期，第一列为最高气温    
    dates, highs, lows = [], [], []
    for row in reader: # 从第2行开始遍历每一行，因为第一行前面已经采用next读取了
        # 使用try-except-else代码块处理缺少数据的问题
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)  
            lows.append(low)


# 根据最高气温数据绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5, linewidth=2, ls='-')
plt.plot(dates, lows, c='blue', alpha=0.5, linewidth=1, ls='-')
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# 设置图形的格式
title = "Daily high and low temperature - 2014\nDeath Valley, CA"
plt.title(title, fontsize=20)
plt.xlabel("Date", fontsize=16)
plt.ylabel("Temperature(F)", fontsize=16)
plt.ylim(10, 120) # 设置y轴坐标范围

#设置坐标轴范围及刻度
my_y_ticks = np.arange(10, 120, 10)
plt.yticks(my_y_ticks)

fig.autofmt_xdate() # 将x轴的文字斜着显示
plt.tick_params(axis='both', which='both', width=2, 
        colors='black', direction='in', labelsize=8)


plt.show()
            

