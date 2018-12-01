#! /usr/bin/env python

from collections import Counter

with open('/where_i_write_hacky_code/advent/day_11/input_file.txt') as f:
    data = f.read().strip().split(',')

highest_value = 0

for i in range(len(data)):
    directions = Counter(data[:i+1])
    n = directions['n'] - directions['s']
    nw = directions['nw'] - directions['se']
    ne = directions['ne'] - directions['sw']

    answer = abs(n) + max(abs(nw), abs(ne))
    if answer > highest_value:
        highest_value = answer

print(highest_value)
