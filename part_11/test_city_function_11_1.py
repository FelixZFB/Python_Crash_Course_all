# -*- coding: cp936 -*-
# 测试代码

import unittest
from city_functions_11_1 import get_city_name

class NamesTestCase(unittest.TestCase):
    """测试name_function_1.py"""
    
    def test_city_name(self):
        """能够正确的处理像Janis Joplin这样的姓名吗？"""
        city_name = get_city_name('chengdu', 'China')
        self.assertEqual(city_name, 'Chengdu China')
    

unittest.main()


