# Using while for iteration
limit = 10
i = 0
while(i <= limit):
    print(f"Iteration {i}")
    i += 1

# Using infinite loop
loop = True
while(loop):
    print("Do you want to stop the loop? [1/0]: ")
    ans = int(input())

    if ans == 1:
        break
    elif ans == 0:
        continue
    else:
        print("It's an error but the loop keeps going by the way")