rivers = {
    'Huanghe': 'China',
    'Nile': 'Egypt',
    'Henhe': 'India',
    'Changjiang': 'China',
    }

for key, value in rivers.items():
    print("The " + key + " runs through " + value + ".")

for key in rivers.keys():
    print(key)

for value in rivers.values():
    print(value)
    
for key in sorted(rivers.keys()):
    print(key)

for value in set(rivers.values()):
    print(value)
