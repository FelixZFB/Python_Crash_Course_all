# -*- coding: cp936 -*-

# 以不同的方式打开文件，并显示出他们


file_name = "learning_python.txt"

# 方法1，全部读取打开
with open(file_name) as file_object:
    content = file_object.read()
    print(content)
    
# 方法2，一次打开一行
with open(file_name) as file_object:
    content = file_object.readline()
    print(content)

# 采用循环的方式，依次打开每一行
with open(file_name) as file_object:
    while True:
        content = file_object.readline()
        print(content)
        if not content:
            break
            
# 方法3，每次一行的方式读取整个文件，并将每行作为一个元素存储在一个列表中
# 可以采用for循环读取列表中的所有元素
with open(file_name) as file_object:
    contents = file_object.readlines()
    print(contents)

pi_string = ''
for content in contents:
    pi_string += content.strip()

print(pi_string)
pi_string.replace('love','hate')
print("\n" + pi_string)



# 方法4，采用fileinput模块
import fileinput
for line in fileinput.input("learning_python.txt"):
    print(line)



       
aaa = "www.w3cschool.cc"
print ("菜鸟教程旧地址：", aaa)
print ("菜鸟教程新地址：", aaa.replace("w3cschool.cc", "runoob.com"))

aaa = "this is string example....wow!!!"
print (aaa.replace("is", "was", 3))  


aaa = "I reallly like dogs."
aaa = aaa.replace("dogs", "cats")
print (aaa) 

