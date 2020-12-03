#! /usr/bin/env python

with open('./data.txt') as f:
    lines = f.read().split()


horizontal_position = 0
vertical_position = 0
tree_count = 0


while True:
    if vertical_position >= len(lines):
        break

    horizontal_index = horizontal_position % len(lines[0])

    if lines[vertical_position][horizontal_index] == '#':
        tree_count += 1

    horizontal_position += 3
    vertical_position += 1


print(tree_count)
