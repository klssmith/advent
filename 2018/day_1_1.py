#! /usr/bin/env python

with open('./data.txt') as f:
    data = f.readlines()


frequency = 0

for instruction in data:
    if instruction[0] == '+':
        frequency += int(instruction[1:])
    else:
        frequency -= int(instruction[1:])

print(frequency)
