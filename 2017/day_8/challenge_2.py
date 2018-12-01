#! /usr/bin/env python

with open('/where_i_write_hacky_code/advent/day_8/input_file.txt') as f:
    data = f.read()

data = data.rstrip().split('\n')

registers = {}
highest_value_held = 0

for line in data:
    line = line.split()
    registers[line[0]] = registers.get(line[0], 0)
    registers[line[4]] = registers.get(line[4], 0)

    condition = '{} {} {}'.format(registers[line[4]], line[5], line[6])

    if eval(condition):
        if line[1] == 'inc':
            registers[line[0]] += int(line[2])
        elif line[1] == 'dec':
            registers[line[0]] -= int(line[2])

        if registers[line[0]] > highest_value_held:
            highest_value_held = registers[line[0]]

print(highest_value_held)
