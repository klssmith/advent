#! /usr/bin/env python

with open('/where_i_write_hacky_code/advent/day_2/input_file.txt') as f:
    data = f.read()

data = data.rstrip().split('\n')

lines_list = [line.split('\t') for line in data]
lines_list = [[int(item) for item in row] for row in lines_list]


def get_row_result(row):
    for number in row:
        row_copy = row[:]
        row_copy.remove(number)

        if any(number % item == 0 for item in row_copy):
            return ([(number // item) for item in row_copy if number % item == 0])


row_results = list(map(get_row_result, lines_list))
checksum = sum([item for sublist in row_results for item in sublist])

print(checksum)
