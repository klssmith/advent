#! /usr/bin/env python

from itertools import cycle


with open('./data.txt') as f:
    data = f.readlines()

data = cycle(data)

frequency = 0
things_seen = []

while True:
    instruction = next(data)

    if frequency in things_seen:
        result = frequency
        break
    else:
        things_seen.append(frequency)

    if instruction[0] == '+':
        frequency += int(instruction[1:])
    else:
        frequency -= int(instruction[1:])

print(result)
