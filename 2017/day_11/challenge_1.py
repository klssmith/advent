#! /usr/bin/env python

from collections import Counter

with open('/where_i_write_hacky_code/advent/day_11/input_file.txt') as f:
    data = f.read().strip().split(',')

directions = Counter(data)

n = directions['n'] - directions['s']
nw = directions['nw'] - directions['se']
ne = directions['ne'] - directions['sw']

answer = abs(n) + max(abs(nw), abs(ne))

print(answer)
