# -*- coding: cp936 -*-
# 详细说明见书P142
# 创建一个用户的类

class User():
    
    def __init__(self, first_name, last_name, age, country, login_attempts):
        """初始化用户的信息"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
        self.login_attempts = login_attempts
    
    def describe_user(self):
        """返回整洁的用户信息"""
        print("The user's name is " + self.first_name.title()
                + " " + self.last_name.title() + ".")
        # 涉及到数字，转换成可以显示的值，记住使用str函数
        print("The user's age is " + str(self.age) + ", and come from " 
                + self.country)
    
    def greet_user(self):
        print("Hello, " + self.first_name.title()
                + " " + self.last_name.title() + ".")
    
    def increment_login_attempts(self):
        self.login_attempts += 1
        print(self.login_attempts)
        
    def reset_login_attempts(self):
        self.login_attempts = 0
        print(self.login_attempts)
                
user_1 = User('felix', 'zhang', 28, 'China', 25)
user_1.describe_user()
user_1.greet_user()
user_1.increment_login_attempts()
user_1.reset_login_attempts()
        
        
                
 


