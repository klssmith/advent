#! /usr/bin/env python

with open('/where_i_write_hacky_code/advent/day_7/input_file.txt') as f:
    data = f.read()

data = data.rstrip().split('\n')

parent_nodes = set()
child_nodes = set()

for line in data:
    parent_nodes.add(line.split()[0])

    if '->' in line:
        children = line.split('->')[-1].split(',')
        for child in children:
            child_nodes.add(child.strip())

root_node = list(parent_nodes ^ child_nodes)[0]

print(root_node)
