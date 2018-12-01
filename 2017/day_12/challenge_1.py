#! /usr/bin/env python

with open('/where_i_write_hacky_code/advent/day_12/input_file.txt') as f:
    data = f.read().strip().split('\n')

store = {}

for line in data:
    key, values = line.split(' <-> ')
    key = int(key)
    values = [int(x) for x in values.split(',')]
    store[key] = values

already_counted = []


def count_linked_pipes(key):
    if key in already_counted:
        return
    else:
        already_counted.append(key)
        for child in store[key]:
            count_linked_pipes(child)


count_linked_pipes(0)
print(len(already_counted))
