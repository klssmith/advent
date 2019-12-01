#! /usr/bin/env python

with open('./data.txt') as f:
    data = f.readlines()

module_mass = [int(line) for line in data]


def fuel_for_module(mass):
    fuel_required = mass // 3 - 2

    if fuel_required <= 0:
        return 0

    return fuel_required + fuel_for_module(fuel_required)


result = sum(
    fuel_for_module(mass) for mass in module_mass
)

print(result)
