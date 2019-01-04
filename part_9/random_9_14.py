# -*- coding: cp936 -*-
# 详细说明见书P159
# 导入标准库中的类

from random import randint

x = randint(1,20)
print(x)

y = randint(1,20)
print(y)

import random

for i in range(20):
    print('%04.3f' % random.random(), end=' ')

