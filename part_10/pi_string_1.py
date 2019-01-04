# -*- coding: cp936 -*-

# 打开100万位的文件
filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
    print(lines[:3])
    
pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string[:52] + "...")
print(len(pi_string))

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of Pi!")
else:
    print("Your birthday does not appear in the fristmillion digits of Pi!")
