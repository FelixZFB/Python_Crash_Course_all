# -*- coding: cp936 -*-
# 详细说明见书P156
# 导入类

from car_new import ElectricCar

my_tesla = ElectricCar('tesla', 'model s', 2016)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()



