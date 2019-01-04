# -*- coding: cp936 -*-
# 详细说明见书P153,导入类,car_new是一个含有编好Car类的python文件

from car_new import Car

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()


