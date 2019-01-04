# -*- coding: cp936 -*-
# 写入用户输入的消息

file_name = 'guest.txt'

with open(file_name, 'a') as file_object:
    message = input("What dou you want to see? : ")
    file_object.write(message)
   


    
