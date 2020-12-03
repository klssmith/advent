#! /usr/bin/env python

import math

with open('./data.txt') as f:
    lines = f.read().split()


def count_trees(horizontal_movement, vertical_movement):
    horizontal_position = 0
    vertical_position = 0
    tree_count = 0

    while True:
        if vertical_position >= len(lines):
            break

        horizontal_index = horizontal_position % len(lines[0])

        if lines[vertical_position][horizontal_index] == '#':
            tree_count += 1

        horizontal_position += horizontal_movement
        vertical_position += vertical_movement

    return tree_count


movement_amounts = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]


print(math.prod(
    count_trees(i[0], i[1]) for i in movement_amounts
))
