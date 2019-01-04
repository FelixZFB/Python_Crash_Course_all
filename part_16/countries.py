# -*- coding: cp936 -*-
# 详细见P327
# 导入国别码

from pygal_maps_world.i18n import COUNTRIES

# 按字母顺序遍历国家列表，然后打印国家代码和国家名称
for country_code in sorted(COUNTRIES.keys()):
    print(country_code, COUNTRIES[country_code])

 

