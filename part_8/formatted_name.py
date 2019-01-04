# coding=utf-8
# 详细说明见书P121
# 返回值

def get_formatted_name(first_name, last_name):
    """return the full name"""
    full_name = first_name + ' ' + last_name
    print(full_name.title())
    
get_formatted_name('jimi', 'hendrix')


def get_formatted_name(first_name, last_name):
    """return the full name"""
    full_name = first_name + ' ' + last_name
    return full_name.title()
    
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
