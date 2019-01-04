# -*- coding: cp936 -*-
# 详细见P3451
# 执行API调用，找出Hacker News热门的文章

import requests
import pygal 
from operator import itemgetter
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# 执行API调用并存储响应
url = 'https://hacker-news.firebaseio.com/v0/'
r = requests.get(url)
print("Status code:", r.status_code)




 

