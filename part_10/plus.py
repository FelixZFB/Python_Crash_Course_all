print("Give me teo numbers, and I will plus them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nThe first number: ")
    if first_number == 'q':
        break
    second_number = input("The second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) + int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0")
    else:
        print(answer)
