# Input data
data = []

xdata = int(input("Enter total data count: "))
for i in range(0, xdata):
    val = int(input(f"Value of data {i + 1}: "))
    data.append(val)
total_data = len(data)

# Sorting
for i in range(0, xdata):
    for j in range(i, xdata):
        if data[i] > data[j]:
            temp = data[i]
            data[i] = data[j]
            data[j] = temp

# Q2
if xdata % 2 == 0:
    mid = [data[xdata // 2 - 1], data[xdata // 2]]
    q_2 = (mid[0] + mid[1]) / 2
    print(f"Value of Q2: {q_2}")
else:
    q_2 = data[xdata // 2]
    print(f"Value of Q2: {q_2}")

# Q1
x_lower = []
for i in range(0, xdata // 2):
    x_lower.append(data[i])
total_lower = len(x_lower)

if total_lower % 2 == 0:
    lower_mid = [x_lower[total_lower // 2 - 1], x_lower[total_lower // 2]]
    q_1 = (lower_mid[0] + lower_mid[1]) / 2
    print(f"Value of Q2: {q_1}")
else:
    q_1 = x_lower[total_lower // 2]
    print(f"Value of Q2: {q_1}")

# Q3 
x_upper = []
for i in range(total_lower, total_data):
    x_upper.append(data[i])
total_upper = len(x_upper)

if total_upper % 2 == 0:
    upper_mid = [x_upper[total_upper // 2 - 1], x_upper[total_upper // 2]]
    q_3 = (upper_mid[0] + upper_mid[1]) / 2 + 1
    print(f"Value of Q2: {q_3}")
else:
    q_3 = x_upper[total_upper // 2]
    print(f"Value of Q3: {q_3}")

# IQR
iqr = q_3 - q_1
print(f"Value of IQR: {iqr}")