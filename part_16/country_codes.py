# -*- coding: cp936 -*-
# 详细见P327
# 编写一个获得国家代码的模块


from pygal_maps_world.i18n import COUNTRIES

def get_country_code(country_name):
    """根据指定的国家，返回Pygal使用的两个字母的国别码"""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
        elif country_name == 'Yemen, Rep.':
            return 'ye'
        elif country_name == 'Macedonia, FYR':
            return 'mk'
        elif country_name == 'Macao SAR, China':
            return 'mo'
        elif country_name == 'Lao PDR':
            return 'la'
        elif country_name == 'Kyrgyz Republic':
            return 'kg'
        elif country_name == 'Korea, Rep.':
            return 'kr'
        elif country_name == 'Korea, Dem. Rep.':
            return 'kp'
        elif country_name == 'Iran, Islamic Rep.':
            return 'ir'
        elif country_name == 'Gambia, The':
            return 'gm'
        elif country_name == 'Egypt, Arab Rep.':
            return 'eg'
        elif country_name == 'Congo, Dem. Rep.':
            return 'cd'
        elif country_name == 'Congo, Rep.':
            return 'cg'
        elif country_name == 'Libya':
            return 'ly'
        elif country_name == 'Bolivia':
            return 'bo'
        elif country_name == 'Venezuela, RB':
            return 've'
        elif country_name == 'Tanzania':
            return 'tz'
        elif country_name == 'Vietnam':
            return 'vn'
    # 如果没有找到指定的国家，就返回None
    return None



