# coding=utf-8
# 按位置传递实参
# 详细说明见书P116

# 位置实参
def describe_pet(animal_type, pet_name):
    """display the information of my pet"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
    
describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
    
# 关键字实参
def describe_pet(animal_type, pet_name):
    """display the information of my pet"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
    
describe_pet(animal_type = 'hamster', pet_name = 'harry')
describe_pet(pet_name = 'harry', animal_type = 'hamster')

# 默认值，动物类型默认为狗
def describe_pet(pet_name, animal_type = 'dog'):
    """display the information of my pet"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
    
describe_pet(pet_name = 'harry')


