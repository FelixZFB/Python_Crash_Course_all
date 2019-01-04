motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles[1] = 'bmw'
print(motorcycles)

motorcycles = ['honda','yamaha','suzuki']
motorcycles.append('ducati')
print(motorcycles)

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
motorcycles.append('bmw')
print(motorcycles)

motorcycles = ['honda','yamaha','suzuki']
motorcycles.insert(0,'ducati')
print(motorcycles)
del motorcycles[1] 

motorcycles = ['honda','yamaha','suzuki']
del motorcycles[0] 
print(motorcycles)

motorcycles = ['honda','yamaha','suzuki']
del motorcycles[1] 
print(motorcycles)

motorcycles = ['honda','yamaha','suzuki']
motorcycles.pop()
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(popped_motorcycle)

motorcycles = ['honda','yamaha','suzuki']
last_owned = motorcycles.pop()
message = "The last motorcycle I owned was a " + last_owned.title() + "."
print(message)

motorcycles = ['honda','yamaha','suzuki']
last_owned = motorcycles.pop(0)
message = "The last motorcycle I owned was a " + last_owned.title() + "."
print(message)

motorcycles = ['honda','ducati','yamaha','suzuki']
motorcycles.remove(motorcycles[1])
print(motorcycles)

motorcycles = ['honda','ducati','yamaha','suzuki']
motorcycles.remove('ducati')
print(motorcycles)

motorcycles = ['honda','ducati','yamaha','suzuki']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
message = "\nA " + too_expensive.title() + " is too expensive for me."
print(motorcycles)
print(message)


