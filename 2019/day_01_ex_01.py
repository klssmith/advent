#! /usr/bin/env python

with open('./data.txt') as f:
    data = f.readlines()

module_mass = [int(line) for line in data]

result = sum(
    mass // 3 - 2 for mass in module_mass
)

print(result)
