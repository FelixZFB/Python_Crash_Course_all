# coding=utf-8
# 详细说明见书P126

# 传递列表，使用函数问候列表中的每一个人
def greet_users(names):
    """greet to everyone"""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)


