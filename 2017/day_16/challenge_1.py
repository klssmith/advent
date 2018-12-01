#! /usr/bin/env python

with open('/where_i_write_hacky_code/advent/day_16/input_file.txt') as f:
    data = f.read().strip().split(',')

programs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']


def spin(programs, amount):
    return programs[-amount:] + programs[:-amount]


def exchange(programs, position_a, position_b):
    programs[position_a], programs[position_b] = programs[position_b], programs[position_a]
    return programs


def partner(programs, a, b):
    position_a = programs.index(a)
    position_b = programs.index(b)
    return exchange(programs, position_a, position_b)


for instruction in data:
    if instruction[0] == 's':
        programs = spin(programs, int(instruction[1:]))
    elif instruction[0] == 'p':
        a, b = instruction[1:].split('/')
        programs = partner(programs, a, b)
    elif instruction[0] == 'x':
        a, b = instruction[1:].split('/')
        programs = exchange(programs, int(a), int(b))

print(''.join(programs))
