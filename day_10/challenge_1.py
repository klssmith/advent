#! /usr/bin/env python

with open('/where_i_write_hacky_code/advent/day_10/input_file.txt') as f:
    data = f.read().strip().split(',')

lengths = [int(x) for x in data]
nums = [x for x in range(256)]
current_position = 0
skip_size = 0


for length in lengths:
    # work out which section needs reversing
    things_to_reverse = []
    start_index_of_things_to_reverse = current_position
    for i in range(length):
        try:
            nums[start_index_of_things_to_reverse]
        except IndexError:
            things_to_reverse.append(nums[start_index_of_things_to_reverse - len(nums)])
        else:
            things_to_reverse.append(nums[start_index_of_things_to_reverse])
        start_index_of_things_to_reverse += 1

    # add the reversed section back in the right place
    start_index_of_things_to_add = current_position
    for j in range(length):
        try:
            nums[start_index_of_things_to_add]
        except IndexError:
            nums[start_index_of_things_to_add - len(nums)] = things_to_reverse.pop()
        else:
            nums[start_index_of_things_to_add] = things_to_reverse.pop()
        start_index_of_things_to_add += 1

    current_position += length + skip_size
    if current_position > len(nums):
        current_position %= len(nums)
    skip_size += 1

print(nums[0] * nums[1])
