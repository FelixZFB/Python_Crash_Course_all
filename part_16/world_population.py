# -*- coding: cp936 -*-
# 详细见P325
# 分析JSON文件

import json 
import pygal
import pygal_maps_world
from country_codes import get_country_code
from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS


# 将数据加载到一个列表中
filename = 'population_data.json'
with open(filename) as f:
    # 读取文件中的数据，读取的结果为一个列表，列表中每一个元素都是一个字典
    pop_data = json.load(f)
    

# 创建一个包含每个国家人口数量的字典
cc_population = {}
# 遍历列表中的每一个字典，里面有一个国家不同年份的数据，选取2010年份的数据
for pop_dict in pop_data:
    # 键年份对应的值是否为2010，原始数据2010为字符串，所以都是字符串比较
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        # 由于原始数据中存在小数，先将数据转换为浮点数，然后转换成整数
        population = int(float(pop_dict['Value']))
        # pygal只能使用两个字母的国别码，JSON中提供的是3位的，定义一个方法获得2位的国别码
        code = get_country_code(country_name)
        if code:
            # 如果国家码存在，将国家码作为键，人口数量作为值，存储在字典中
            cc_population[code] = population
        else:
            # 数据中有些国家名称书写的和pygal格式不一致，虽然有数据，但是不能获得国家码，打印一个提示消息
            print('ERROR - ' + country_name)

# 根据人口数量将所有的国家分组
cc_pops_1, cc_pops_2, cc_pops_3, cc_pops_4 = {}, {}, {}, {}
for cc, pop in cc_population.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 100000000:
        cc_pops_2[cc] = pop
    elif pop < 1000000000:
        cc_pops_3[cc] = pop
    else:
        cc_pops_4[cc] = pop

# 看看每个分组包含多少个国家
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3), len(cc_pops_4))



wm_style = RS('#336699', base_style=LCS)
wm = pygal_maps_world.maps.World(style=wm_style)

wm.title = 'World Population in 2010, by Country'
wm.add('0-10m', cc_pops_1)
wm.add('10m-100m', cc_pops_2)
wm.add('100m-1bn', cc_pops_3)
wm.add('>1bn', cc_pops_4)

wm.render_to_file('World_Population.svg')
 

