# coding=utf-8
# 按位置传递实参
# 详细说明见书P119

# 位置实参、关键字实参和默认值可以混合使用
def describe_pet(pet_name, animal_type = 'dog'):
    """display the information of my pet"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# 一条名为Willie的小狗(下面两种方式输出结果一致)
# 位置实参和调用默认值
describe_pet('willie')

# 关键字实参和调用默认值
describe_pet(pet_name = 'willie')

# 一只名为Harry的仓鼠(实参混用)(下面三种方式输出结果一致)
# 位置实参替换默认值
describe_pet('harry', 'hamster')

# 关键字实参
describe_pet(pet_name = 'harry', animal_type = 'hamster')

# 关键字实参位置调换
describe_pet(animal_type = 'hamster', pet_name = 'harry')





