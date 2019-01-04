# coding=utf-8
# 详细说明见书P137
# 导入模块

from printing_models import print_models as p, show_completed_models as s

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
p(unprinted_designs[:], completed_models)
s(completed_models)


