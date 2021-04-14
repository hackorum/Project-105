import csv, math
with open('csv/data.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data = file_data[0]


def get_mean(data):
    length = len(data)
    total = 0
    for i in data:
        total += int(i)
    mean = total / length
    return mean


squared_list = []
for data in file_data:
    sub = int(data) - get_mean(data)
    sub = sub**2
    squared_list.append(sub)

total = 0
for j in squared_list:
    total += j
n = len(file_data)
n -= 1

res = total / n

std = math.sqrt(res)

print(std)