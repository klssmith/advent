#! /usr/bin/env python

with open('./data.txt') as f:
    data = f.readlines()


numbers = [int(line) for line in data]

a = None
b = None

for num in numbers:
    num_to_find = 2020 - num

    if num_to_find in numbers:
        a = num
        b = num_to_find
        break


print(a * b)
