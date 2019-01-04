#_*_coding:cp936_*_
# 定义一个函数
# 详细说明见书P114

def greet_user():
    '''显示简单的问候语'''
    print("Hello!")

greet_user()

def greet_user(username):
    # 显示简单的问候语
    print("Hello! " + username.title() + "!")

greet_user('jessle')
greet_user('felix')
