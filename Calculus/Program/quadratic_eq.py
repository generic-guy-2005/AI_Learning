import math

# Program to found properties of quadratic formula

while(True):
    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))
    c = int(input("Enter value of c: "))

    # Construct the function
    print(f"Created function:\nf(x) = {a}x^2 + ({b})x + ({c})\n")

    # Axis of symmetry
    axisOfSym = -1 * (b / (2 * a))
    print(f"Axis of Symmetry: {axisOfSym}")

    # Vertex
    vertex = pow(axisOfSym, 2) + (b * axisOfSym) + c
    print(f"Vertex: ({axisOfSym}, {vertex})")

    # y-intercept
    print(f"Y-intercept: {c}")

    # x-intercept
    x1 = ((-1 * b) + math.sqrt((pow(b, 2)) - (4 * a * c))) / 2 * a
    x2 = ((-1 * b) - math.sqrt((pow(b, 2)) - (4 * a * c))) / 2 * a
    print(f"X-intercept: ({x1}, 0) or ({x2}, 0)")

    print("Would you like to continue? y/n ", end='')
    ans = input()

    if ans == "n" or ans == "N":
        break

print("Exiting...")