#! /usr/bin/env python

from collections import defaultdict

with open('/where_i_write_hacky_code/advent/day_4/input_file.txt') as f:
    data = f.read()

data = data.rstrip().split('\n')

total_valid_passphrases = 0

for line in data:
    line = line.split()

    line = [''.join(sorted(i)) for i in line]

    result = defaultdict(int)
    for word in line:
        result[word] += 1

    if not any(value > 1 for _key, value in result.items()):
        total_valid_passphrases += 1

print(total_valid_passphrases)
