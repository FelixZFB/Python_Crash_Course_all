# -*- coding: cp936 -*-
# 详细见P329
# 制作世界地图，在地图上显示数字数据
# 显示北美国家的人口数据

import pygal 
import pygal_maps_world.maps


wm = pygal_maps_world.maps.World()
wm.title = 'Population of Countries in North America'
wm.add('North America', {'ca': 34126000, 'mx': 309349000, 'us': 113423000})

wm.render_to_file('na_population.svg')

