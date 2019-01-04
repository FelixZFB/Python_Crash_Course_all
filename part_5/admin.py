names = ['Eric','Felix','Admin','Jodan']
for name in names:
    if name == 'Admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello " + name + ", thank you for logging in again.")

names = []
if names:
    for name in names:
        print("Hello " + name + ", thank you for logging in again.")
else:
    print("We need to find some users.")
    
