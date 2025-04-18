# Control structure

decision = int(input("Insert a number [1 = Y, 0 = N]: "))

if decision:
    print("Your decision: Yes")
else:
    print("Your decision: No")

# Comparison operator

number = int(input("Insert a number [0-100]: "))

if number > 50:
    print("The number is greater than 50")
elif number == 50:
    print("The number is equal to 50")
else:
    print("The number is less than 50")