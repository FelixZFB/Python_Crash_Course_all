# -*- coding: cp936 -*-
# 详细见P318
# 分析CSV文件

import csv
from datetime import datetime
from matplotlib import pyplot as plt


filename = 'sitka_weather_2014.csv'
with open(filename) as f:
    
    # 读取整个文件的内容
    reader = csv.reader(f)
    
    # 读取文件的第一行内容
    header_row = next(reader)

    # 打印文件头及其位置，索引是第几列，及其对应的内容
    for index, column_header in enumerate(header_row):
        print(index, column_header)

    # 上面输出显示获取文件中的最高气温，上面输出显示，第0列为日期，第一列为最高气温    
    dates, highs = [], []
    for row in reader: # 从第2行开始遍历每一行，因为第一行前面已经采用next读取了
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)
        high = int(row[1])
        highs.append(high)  # 将每行的索引1处的数据，实际为表格的第二列最高气温添加到列表中

# 根据最高气温数据绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red')

# 设置图形的格式
plt.title("Daily high temperature, 2014")
plt.xlabel("Date", fontsize=16)
fig.autofmt_xdate() # 将x轴的文字斜着显示
plt.ylabel("Temperature(F)", fontsize=16)
plt.tick_params(axis='minor', which='both', width=2, 
        colors='gold', direction='in', labelsize=8)

plt.show()
            

