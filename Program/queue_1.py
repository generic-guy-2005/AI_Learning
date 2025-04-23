# Import
from collections import deque

# Creation
queue = deque()

# Enqueue
for i in range(0, 4):
    num = int(input("Enter a number: "))
    queue.append(num)

print(f"Created queue: {queue}")

# Dequeue
removed = queue.popleft()

print(f"First added value {removed} is removed")
print(f"Value remains in queue: {queue}")