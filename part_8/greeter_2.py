# coding=utf-8
# 详细说明见书P125

# 返回值为字典
def get_formatted_name(first_name, last_name):
    """return to full name"""
    full_name = first_name + ' ' + last_name
    return full_name.title()

# 这是一个无限循环,输入姓和名，打印出第一个全名后，进入到下一个循环，添加退出语句
while True:
    print("\nPlease tell me your name: ")
    print("(Enter 'q' at any time to quit)")
    
    f_name = input("First name: ")
    if f_name == 'q':
        break
        
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    
    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")

