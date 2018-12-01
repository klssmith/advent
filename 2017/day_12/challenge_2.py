#! /usr/bin/env python

with open('/where_i_write_hacky_code/advent/day_12/input_file.txt') as f:
    data = f.read().strip().split('\n')

store = {}
groups = 0

for line in data:
    key, values = line.split(' <-> ')
    key = int(key)
    values = [int(x) for x in values.split(',')]
    store[key] = values


def count_linked_pipes(key):
    if key in already_seen:
        return
    else:
        already_seen.append(key)
        for child in store[key]:
            count_linked_pipes(child)


while store:
    key = min(store)
    already_seen = []

    count_linked_pipes(key)

    for item in already_seen:
        del store[item]

    groups += 1

print(groups)
