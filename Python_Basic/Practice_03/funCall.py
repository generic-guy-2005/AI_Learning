# Using function to repeat the same code of block

def process(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

while True:
    num = int(input("Choose a random number: "))
    print(f"The number entered is: {process(num)}")

    again = bool(int(input("Again? [1/0]: ")))
    if not again:
        break