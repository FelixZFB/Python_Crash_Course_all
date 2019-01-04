# -*- coding: cp936 -*-

# 打开同一个文件夹下的文档
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)

# 采用绝对路径打开文档，正常是斜杠，如果打开错误换成反斜杠
file_path = 'C:/Users/HP/Desktop/python_work/part_10/pi_digits.txt'
with open(file_path) as file_object:
    contents = file_object.read()
    print(contents)

# 打开文件，以每次一行的方式检查文件
file_name = 'pi_digits.txt'
with open(file_name) as file_object:
    for line in file_object:
        print(line)

# 打开文件，以每次一行的方式检查文件，print语句后面也有一个换行符,默认文件末尾有一个换行符
# 使用rstrip()函数消除换行符
file_name = 'pi_digits.txt'
with open(file_name) as file_object:
    for line in file_object:
        print(line.rstrip())

# 打开文件，逐字检查
file_name = 'pi_digits.txt'
with open(file_name) as file_object:
    for line in file_object.read():
        print(line.rstrip())

# 将打开的各行存储到一个列表中，并且可以在with代码块之外使用这个列表
file_name = 'pi_digits.txt'

with open(file_name) as file_object:
    lines = file_object.readlines()
    
for line in lines:
        print(line.rstrip())
