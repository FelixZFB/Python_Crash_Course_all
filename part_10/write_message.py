# -*- coding: cp936 -*-
# 写入文件

file_name = 'programming.txt'

with open(file_name, 'w') as file_object:
    file_object.write("I love programming.")
    aaa = 111
    file_object.write(str(aaa))
    
with open(file_name, 'w') as file_object:
    file_object.write("I love programming.")
    aaa = 111
    file_object.write(str(aaa))
