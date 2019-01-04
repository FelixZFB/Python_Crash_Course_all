# -*- coding: cp936 -*-
# 详细见P329
# 制作世界地图

import pygal 
import pygal_maps_world.maps


wm = pygal_maps_world.maps.World()
wm.title = 'North, Central, and South America'

wm.add('North America', ['ca', 'mx', 'us'])
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'ec', 'gf', 
    'gy', 'pe', 'py', 'sr', 'uy', 've'])

wm.render_to_file('americas.svg')

