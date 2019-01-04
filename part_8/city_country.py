# coding=utf-8
# 详细说明见书P125

# 返回值为字典
def get_formatted_name(first_name, last_name):
    """return to full name"""
    full_name = first_name + ' ' + last_name
    return full_name.title()


    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")

