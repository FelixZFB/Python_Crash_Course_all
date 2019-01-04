# coding=utf-8
# 详细说明见书P125

# 返回值为字典
def city_country(city, country):
    """return to full name"""
    full_name = city + ', ' + country
    return full_name.title()


aaa = city_country('santiago', 'chile')
print(aaa)

