#! /usr/bin/env python

with open('./data.txt') as f:
    data = f.readlines()


counter = 0

for line in data:
    nums, letter, password = line.split()
    minimum, maximum = (int(x) for x in nums.split('-'))
    letter = letter[0]

    letter_count = password.count(letter)

    if letter_count >= minimum and letter_count <= maximum:
        counter += 1


print(counter)
