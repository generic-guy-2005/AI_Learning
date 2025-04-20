def add(a, b):
    print(a + b)

def sub(a, b):
    print(a - b)

def mul(a, b):
    print(a * b)

def div(a, b):
    print(a / b)

while True:
    a = int(input("Value a: "))
    b = int(input("Value b: "))

    print("Select operation:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")
    choice = int(input("Choice: "))

    if choice == 1:
        add(a, b)
    elif choice == 2:
        sub(a, b)
    elif choice == 3:
        mul(a, b)
    elif choice == 4:
        div(a, b)
    else:
        print("Error input")

    again = bool(int(input("Try again?: ")))
    if not again:
        break 