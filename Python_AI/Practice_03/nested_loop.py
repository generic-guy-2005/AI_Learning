# Advanced loop combining all loops that have been learned

loop = True
while(loop):
    print("What to do?\n1. 10 times iteration\n2. Even number iteration\n3. Exit")
    ans = int(input("Choice: "))

    if ans == 1:
        for i in range(1, 11):
            print(f"Iteration: {i}")
    elif ans == 2:
        for i in range(1, 11):
            if i % 2 == 0:
                print(f"Even Iteration: {i}")
            else:
                continue
    elif ans == 3:
        print("Exiting...")
        loop = False
    else:
        print("Error Input: Loop Continued")

print("End of Program")