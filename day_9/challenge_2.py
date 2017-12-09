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

# remove garbage from data and store it
garbage = []

while '<' in data:
    a = data.index('<')
    b = data.index('>')
    garbage.append(data[a:b + 1])
    data = data[:a] + data[b + 1:]

# sum the number of non-cancelled characters in garbage
total = 0

for i in garbage:
    total += (len(i) - 2)


print(total)
