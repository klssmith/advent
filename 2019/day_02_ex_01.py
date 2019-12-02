#! /usr/bin/env python

with open('./data.txt') as f:
    data = [int(i) for i in f.read().split(',')]


data[1] = 12
data[2] = 2


for i in range(0, len(data), 4):
    if data[i] == 1:
        position_1 = data[i + 1]
        position_2 = data[i + 2]
        position_3 = data[i + 3]
        data[position_3] = data[position_1] + data[position_2]
    elif data[i] == 2:
        position_1 = data[i + 1]
        position_2 = data[i + 2]
        position_3 = data[i + 3]
        data[position_3] = data[position_1] * data[position_2]
    elif data[i] == 99:
        break

print(data[0])
