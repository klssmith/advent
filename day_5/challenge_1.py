#! /usr/bin/env python

with open('/where_i_write_hacky_code/advent/day_5/input_file.txt') as f:
    data = f.read()

data = data.rstrip().split('\n')
data = [int(line) for line in data]

jumps = 0
current_position = 0

while True:
    try:
        destination = data[current_position] + current_position

        data[current_position] += 1
        jumps += 1

        current_position = destination

    except(IndexError):
        break

print(jumps)
