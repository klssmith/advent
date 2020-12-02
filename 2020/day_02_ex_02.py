#! /usr/bin/env python

with open('./data.txt') as f:
    data = f.readlines()


counter = 0

for line in data:
    nums, letter, password = line.split()
    position_1, position_2 = (int(x) for x in nums.split('-'))
    letter = letter[0]

    is_pos_1_match = password[position_1 - 1] == letter
    is_pos_2_match = password[position_2 - 1] == letter

    if len(set([is_pos_1_match, is_pos_2_match])) == 2:
        counter += 1


print(counter)
