# Solve linear equations

slope = None
x1 = 0
x2 = 0
y1 = 0
y2 = 0

def linear_form(slope, b):
    slope = slope * -1

    if slope < 0:
        slope = slope * -1
        b = b * -1
        print(f"Standard Form:\n{round(slope, 2)}x - y = {round(b, 2)}")
    else:
        print(f"Standard Form:\n{round(slope, 2)}x + y = {round(b, 2)}")

    print("--------------------")

def linear_fun(slope=None, x1=None, y1=None, x2=None, y2=None):
    if slope is None:
        slope = (y2 - y1) / (x2 - x1)
        b = y1 - slope * x1

        if slope < 0 and b < 0:
            slope = slope * -1
            b = b * -1
            print(f"y-Intercept Form:\ny = {round(slope, 2)}x + {round(b, 2)}")
        else:
            print(f"y-Intercept Form:\ny = {round(slope, 2)}x + {round(b, 2)}")

    if slope is not None:
        if x1 is None:
            b = y2 - slope * x2
        else:
            b = y1 - slope * x1

        if slope < 0 and b < 0:
            slope = slope * -1
            b = b * -1

        print(f"y-Intercept Form:\ny = {round(slope, 2)}x + {round(b, 2)}")
        print("--------------------")

    linear_form(slope, b)

while True:
    print("What is known from the problem?\n1. Slope (m)\n2. Point A (x_1, y_1)\n3. Point B (x_2, y_2)\n4. Calculate\n0. Exit")
    choice = int(input("Choice: "))

    if choice == 1:
        slope_a = int(input("Enter the value of the slope numerator: "))
        slope_b = int(input("Enter the value of the slope denumerator: "))
        slope = slope_a / slope_b
        print("--------------------")
    elif choice == 2:
        x1 = int(input("Enter x_1 value: "))
        y1 = int(input("Enter y_1 value: "))
        print("--------------------")
    elif choice == 3:
        x2 = int(input("Enter x_2 value: "))
        y2 = int(input("Enyer y_2 value: "))
        print("--------------------")
    elif choice == 4:
        print("--------------------")
        linear_fun(slope, x1, y1, x2, y2)
    elif choice == 0:
        print("Exiting...")
        break
    else:
        print("Error input")
