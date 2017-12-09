#! /usr/bin/env python

with open('/where_i_write_hacky_code/advent/day_9/input_file.txt') as f:
    raw_data = f.read()

# remove each '!' and the following character
data = ''
skip_next_iteration = False

for i in range(len(raw_data)):
    if raw_data[i] == '!' or skip_next_iteration:
        skip_next_iteration = not skip_next_iteration
    else:
        data += raw_data[i]

# remove garbage from data
while '<' in data:
    a = data.index('<')
    b = data.index('>')
    data = data[:a] + data[b + 1:]

# sum the total of the groups
total = 0

for i in range(len(data)):
    if data[i] == '{':
        opening_count = data.count('{', 0, i)
        closing_count = data.count('}', 0, i)
        total += opening_count - closing_count + 1


print(total)
