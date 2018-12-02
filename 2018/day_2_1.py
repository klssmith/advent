#! /usr/bin/env python

from collections import Counter

with open('./data.txt') as f:
    data = f.readlines()


twos = 0
threes = 0

for line in data:
    thing = Counter(line)
    if 2 in thing.values():
        twos += 1
    if 3 in thing.values():
        threes += 1

print(twos * threes)
