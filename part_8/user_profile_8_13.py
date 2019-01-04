# coding=utf-8
# 详细说明见书P132

# 使用任意数量的关键字实参,采用**

def build_profile(first, last, **user_info):
    """print all information"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein', 
                            location = 'princeton', 
                            field = 'physics',
                            country = 'china',
                            city = 'chengdu')
print(user_profile)



