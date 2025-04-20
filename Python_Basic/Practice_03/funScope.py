# Using global and local variable for the function

# Global variable
pi = 3.14

def circleArea(radius):
    global pi

    # Local variable
    result = pi * radius * radius
    return result

radius = int(input("Enter a radius: "))
print(f"Area of circle: {circleArea(radius)}")