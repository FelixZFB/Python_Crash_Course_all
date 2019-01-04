# coding=utf-8
# 详细说明见书P123

# 返回值为字典
def build_person(first_name, last_name):
    """return to a dictionary, include a person's information"""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)

# 返回值为字典,加入可选形参年龄，age有值时，将age加入到字典中
def build_person(first_name, last_name, age = ''):
    """return to a dictionary, include a person's information"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age = 27)
print(musician)

