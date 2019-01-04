# -*- coding: cp936 -*-
# 详细见P325
# 分析JSON文件

import json 
import pygal
from country_codes import get_country_code
from pygal.style import LightColorizedStyle , RotateStyle


filename = 'world_gdp.json'

with open(filename) as f:
    pop_data = json.load(f)
    
world_gdp = {}

for pop_dict in pop_data:
    if pop_dict['Year'] == 2016:
        country_name = pop_dict['Country Name']
        gdp = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            # 如果国家码存在，将国家码作为键，人口数量作为值，存储在字典中
            world_gdp[country_name] = gdp
# print(world_gdp)

# 将GDP按数值分类
low_gdp_name, medium_gdp_name, high_gdp_name, super_gdp_name = [], [], [], []
low_gdp, medium_gdp, high_gdp, super_gdp = [], [], [], []

for cn, gp in world_gdp.items():
    if gp < 15000*100000000:
        print()
    elif gp < 20000*100000000:
        low_gdp_name.append(cn)
        low_gdp.append(gp)
    elif gp < 30000*100000000:
        medium_gdp_name.append(cn)
        medium_gdp.append(gp)
    elif gp < 50000*100000000:
        high_gdp_name.append(cn)
        high_gdp.append(gp)
    else:
        super_gdp_name.append(cn)
        super_gdp.append(gp)

print(low_gdp_name)
print(medium_gdp_name)
print(high_gdp_name)
print(super_gdp_name)

# 不同系列采用不同的颜色
# 第一个参数是16进制的RGB颜色，前两位代表R，中间两位代表G，最后两位代表B。
# 数字越大颜色越深。第二个参数设置基础样式为亮色主题，pygal默认使用较暗的颜色主题
bar_style = RotateStyle('#336699', base_style=LightColorizedStyle)

bar = pygal.Bar(style=bar_style)

bar.title = 'World GDP in 2016'

bar.add('LOW_GDP', low_gdp)
bar.add('MEDIUM_GDP', medium_gdp)
bar.add('HIGH_GDP', high_gdp)
bar.add('SUPER_GDP', super_gdp)

bar.x_title = 'Country Name'
bar.y_title = 'GDP of Country'
bar.render_to_file('World GDP in 2016.svg')

 

