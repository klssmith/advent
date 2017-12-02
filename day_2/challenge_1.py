#! /usr/bin/env python

with open('/where_i_write_hacky_code/advent/day_2/input_file.txt') as f:
    data = f.read()

data = data.rstrip().split('\n')

lines_list = [line.split('\t') for line in data]
lines_list = [[int(item) for item in row] for row in lines_list]

checksum = sum([max(row) - min(row) for row in lines_list])

print(checksum)
