# -*- coding: cp936 -*-
# 使用json.dump()存储数据

import json

numbers = [1, 3, 5, 7, 11, 13]

filename = 'number.json'
with open(filename) as f_obj:
   numbers = json.load(f_obj)
   
print(numbers)
    




    
