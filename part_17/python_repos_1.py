# -*- coding: cp936 -*-
# 详细见P345
# 执行API调用，找出GitHub上评分最高的项目

import requests
import pygal 
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# 执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)

# 打印一个状态码，看请求网址是否成功
print("Status code:", r.status_code)

# 获取到的网址信息，其实就是一个类似字典的信息，将API响应存储在一个字典中
response_dict = r.json()
# 处理结果,打印出获取的到字典中的键，和网页对比，发现没有问题
print(response_dict.keys())
print("Total repositories:", response_dict['total_count']) # 打印总条目

# 探索有关仓库的信息,items对应的是一个列表，列表中包含很多字典
repo_dicts = response_dict['items']

# 可视化仓库的信息,将仓库名称和对应评分提取到列表中
names, stars = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

my_style = LS('#993366', base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 30
my_config.show_legend = True
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names
chart.add('Stars', stars)
chart.render_to_file('Python_repos_1.svg')


 

