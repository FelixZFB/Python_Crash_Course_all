# -*- coding: cp936 -*-

# 使用打开文件中的值
file_name = 'pi_digits.txt'

with open(file_name) as file_object:
    lines = file_object.readlines()

# 先读取第一行，pi_string就等于第一行字符串，然后读取第二行，加到这个字符串上，直到循环结束
pi_string = ''    
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))

# 删除所有的空格可以使用strip()
pi_string = ''    
for line in lines:
    pi_string += line.strip()

print("\n" + pi_string)
print(len(pi_string))

# 将打开的文件存储在一个列表中，代码块之后还可以使用
with open(file_name) as file_object:
    lines = file_object.readlines()

for line in lines:
    print("\n" + line.rstrip())



