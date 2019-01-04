# -*- coding: cp936 -*-
# 详细说明见书P142
# 创建一个餐馆的类

class Restaurant():
    
    def __init__(self, restaurant_name, cuisine_type, open_time, favors):
        """初始化描餐馆的属性"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.open_time = open_time
        self.favors = favors
    
    def describe_restaurant(self):
        """返回整洁的描述性信息"""
        print("The restaurant's name is " + self.restaurant_name)
        print("The cuisine_type is " + self.cuisine_type)
    
    def open_restaurant(self):
        if self.open_time >= 10:
            print("The restaurant has opened.")
        else:
            print("The restaurant has closed.")
    
    
        



new_restaurant = Restaurant('Yunxi', 'Chuancai', 20, 'Sweet')
new_restaurant.describe_restaurant()

        
        
                
 


