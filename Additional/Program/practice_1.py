# Description
# Creating a simple task manager using queue as data structure

from collections import deque

tasks = deque()

while True:
    print("What to do today?\n1. Add Task\n2. End Task\n3. View Tasks\n4. Exit\n")
    choice = int(input("Choice: "))

    if choice == 1:
        desc = input("Task description: ")
        tasks.append(desc)
    elif choice == 2:
        done = tasks.popleft()
        print(f"Task {done} completed! Good work!")
    elif choice == 3:
        print(tasks)
    elif choice == 4:
        print("Exiting...")
        break
    else:
        print("Input Error")