# -*- coding: cp936 -*-
# 详细见P340
# 执行API调用，找出GitHub上评分最高的项目

import requests

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
print("\nRepositories returned:", len(repo_dicts))

# 研究第一个仓库，其实就是研究第一个字典
repo_dict = repo_dicts[0]
print("\nKeys:", len(repo_dict))
print()
# for key in sorted(repo_dict.keys()):
    # print(key)

# 提前第一个字典中的关键信息
print("\nSelected information about first repository:")
for repo_dict in repo_dicts:
    print('Name:', repo_dict['name'])
    print('Owner:', repo_dict['owner']['login']) # 字典键对应的值是字典，提取子字典里面的值
    print('Stars:', repo_dict['stargazers_count'])
    print('Repository:', repo_dict['html_url'])
    print('Created:', repo_dict['created_at'])
    print('Updated:', repo_dict['updated_at'])
    print('Description:', repo_dict['description'])
    print()



 

