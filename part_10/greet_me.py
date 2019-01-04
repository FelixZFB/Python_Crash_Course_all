# -*- coding: cp936 -*-
# 使用json.dump()存储数据

import json

filename = 'username.json'
with open(filename) as f_obj:
   username = json.load(f_obj)
   print("Welcome back, " + username + "!")
   




    
