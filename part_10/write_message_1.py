# -*- coding: cp936 -*-
# 写入多行文字

file_name = 'programming.txt'

with open(file_name, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love programming.\n")


    
with open(file_name, 'a') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love programming.\n")
