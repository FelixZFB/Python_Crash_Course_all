# coding=utf-8
# 详细说明见书P130

# 传递任意数量的实参


def make_pizza(*toppings):
    """print all toppings"""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

    
def make_pizza(*toppings):
    """print all toppings"""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')



