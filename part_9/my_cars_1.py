# -*- coding: cp936 -*-
# 详细说明见书P156
# 导入类

import car_new 

my_beetle = car_new.Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = car_new.ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())



