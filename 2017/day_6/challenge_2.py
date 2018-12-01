#! /usr/bin/env python

with open('/where_i_write_hacky_code/advent/day_6/input_file.txt') as f:
    data = f.read()

data = data.split()
banks = [int(x) for x in data]

cycles = []

while banks not in cycles:
    cycles.append(banks)
    banks = banks[:]

    highest_number = max(banks)
    current_bank = banks.index(highest_number)
    banks[current_bank] = 0

    for i in range(highest_number):
        if current_bank == len(banks) - 1:
            current_bank = 0
        else:
            current_bank += 1

        banks[current_bank] += 1

print(len(cycles) - cycles.index(banks))
