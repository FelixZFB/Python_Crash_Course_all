# coding=utf-8
# 详细说明见书P127

# 创建两个函数，打印列表，显示列表
# 打印每个设计，并将其移动到另外一个列表中

def print_models(unprinted_designs, completed_models):
    """print every designs, and then been moved to completed_models"""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        
        #模拟3D打印模型的过程
        print("Printing modeling: " + current_design)
        completed_models.append(current_design)

# 创建一个显示打印好所有模型的函数
def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

# 以下部分为主程序，只需要调用函数即可

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

# 采用切片[:]向函数传递列表副本，原列表仍然保留
print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)
print(unprinted_designs)




