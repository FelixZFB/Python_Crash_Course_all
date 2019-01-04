# coding=utf-8
# 详细说明见书P130

# 使用位置实参和传递任意数量的实参，结合使用

def make_pizza(size, *toppings):
    """print all toppings"""
    print("\nMaking a " + str(size) + 
            "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')



