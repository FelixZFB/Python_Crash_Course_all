# coding=utf-8
# 详细说明见书P122

# 实参不可选
def get_formatted_name(first_name, middle_name, last_name):
    """return the full name"""
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()
    
musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)

# 将实参变成可选的，指定一个空字符串,非空字符串解读为True
def get_formatted_name(first_name, last_name, middle_name = ''):
    """return the full name"""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()
    
musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
