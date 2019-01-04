requested_toppings = ['mushrooms','extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")

requested_toppings = ['mushrooms','green peppers','extra cheese']
for requested_topping in requested_toppings:
    print("Adding " + requested_topping +".")

print("\nFinished making your pizza!")

requested_toppings = ['mushrooms','green peppers','extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'mushrooms':
        print("\nSorry, we are out of mushrooms right now")
    else:
        print("Adding "+ requested_topping +".")
   
print("\nFinished making your pizza!")


