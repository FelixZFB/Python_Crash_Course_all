# coding=utf-8
# 目的：字典中存储列表

#存储所点披萨的信息
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'exttra cheese'],
    }

# 概述所点的披萨
print("You ordered a " + pizza['crust'] + "-crust pizza " + 
    "with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)

# 显示每个人喜欢的语音
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }
print(favorite_languages)

for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())

# 增加if语句，改变输出格式
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }


for name, languages in favorite_languages.items():
    if len(languages) < 2:
        print("\n" + name.title() + "'s favorite languages is " + language.title())
    else:
        print("\n" + name.title() + "'s favorite languages are:")
        for language in languages:
            print("\t" + language.title())
