# -*- coding: cp936 -*-
# 详细说明见书P144
# 创建一个汽车的类
# 修改属性的值，三种不同的方法
# 方法2：通过方法，内部更新属性的值,添加一个逻辑，禁止将里程改小

class Car():
    
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 20
    
    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        """打印出一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")
        
    def update_odometer(self, mileage):
        """将里程表读数设置为指定的值,禁止将里程表读数向回调"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(19)
my_new_car.read_odometer()


