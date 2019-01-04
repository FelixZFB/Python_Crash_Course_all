for value in range(1,10):
	print(value)

numbers = []
for value in range(1,10):
	numbers.append(value)
print(numbers)
print(value)

numbers = []
for value in range(1,1000000):
	numbers.append(value)


numbers = []
for value in range(1,1000001):
	numbers.append(value) 

print(min(numbers))
print(max(numbers))
print(sum(numbers))

numbers = list(range(2,20,2))
print(numbers)

numbers = list(range(1,20,2))
print(numbers)

numbers = []
for number in range(1,20,2):
	numbers.append(number)	
print(numbers)

numbers = list(range(3,30,3))
print(numbers)

numbers = []
for value in range(1,10):
	number = value**3
	numbers.append(number)	
print(numbers)

numbers = [value**3 for value in range(1,10)]
print(numbers)
