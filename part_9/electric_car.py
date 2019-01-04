# -*- coding: cp936 -*-
# 详细说明见书P148
# 类的继承


class Car():
    
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
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
        
    def increment_odometer(self, miles):
        """将里程表读数增加指定的里程"""
        if miles >= 0:
            self.odometer_reading += miles
        else :
            print("You can't roll back an odometer!")

class ElectricCar(Car):
    """电动汽车的独特之处"""
    
    def __init__(self, make, model, year):
        """初始化父类的属性,再初始化电动汽车的特有属性"""
        super().__init__(make, model, year)
        self.battery_size = 70
    
    def describe_battery(self):
        """打印一条消息描述电瓶的容量"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")


my_used_car = Car('audi', 'a4', 2016)
print(my_used_car.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.update_odometer(20)
my_tesla.read_odometer()
my_tesla.describe_battery()

