#! /usr/bin/env python

from knot import knot_hash_encrypt

key = 'amgozmfv'
rows = ['{}-{}'.format(key, i) for i in range(128)]
hashed_rows = [knot_hash_encrypt(row) for row in rows]

grid = []

for row in hashed_rows:
    answer_string = '{0:0128b}'.format(int(row, 16))
    grid.append(list(answer_string))


def mark_the_groups(grid, a, b):
    grid[a][b] = 'x'
    adjacent_squares = []

    adjacent_squares.append((a-1, b)) if a - 1 >= 0 else None
    adjacent_squares.append((a+1, b)) if a + 1 < len(grid[0]) else None
    adjacent_squares.append((a, b-1)) if b - 1 >= 0 else None
    adjacent_squares.append((a, b+1)) if b + 1 < len(grid[0]) else None

    for i in adjacent_squares:
        if grid[i[0]][i[1]] == '1':
            mark_the_groups(grid, i[0], i[1])


groups = 0

for row in range(len(grid)):
    for cell in range(len(grid)):
        if grid[row][cell] == '1':
            mark_the_groups(grid, row, cell)
            groups += 1

print(groups)
