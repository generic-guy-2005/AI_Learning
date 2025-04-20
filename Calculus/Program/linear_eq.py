# Solve linear equations

slope = None

def linear_fun(slope=None, x1=None, y1=None, x2=None, y2=None):
    if slope is None:
        # Using slope formula
        delta_y = y2 - y1
        delta_x = x2 - x1
        m = delta_y / delta_x

        # Using point-slope formula
        if y1 < 0:
            y1 = y1 * -1
            right = y1

        x1 = m * x1
        if x1 < 0:
            x1 = x1 * -1
            left = x1

        result = left + right
        if result > 0:
            value = f"+ {result}"

        print(f"Result:\ny = {m}x {result}")

while True:
    print("What is known from the problem?\n1. Slope (m)\n2. Point A (x_1, y_1)\n3. Point B (x_2, y_2)\n4. Calculate")
    choice = int(input("Choice: "))

    if choice == 1:
        slope = int(input("Enter the value of the slope: "))
    elif choice == 2:
        x1 = int(input("Enter x_1 value: "))
        y1 = int(input("Enter y_1 value: "))
    elif choice == 3:
        x2 = int(input("Enter x_2 value: "))
        y2 = int(input("Enyer y_2 value: "))
    elif choice == 4:
        linear_fun(slope, x1, y1, x2, y2)
    elif choice == 5:
        print(-1 * 1)
    else:
        break
