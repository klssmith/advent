#! /usr/bin/env python

with open('./data.txt') as f:
    data = f.readlines()

def is_one_different(word_1, word_2):
    same = different = 0

    for char_1, char_2 in zip(word_1, word_2):
        if char_1 == char_2:
            same += 1
        else:
            different += 1

    return different == 1


current = None
match = None

while True:
    current = data.pop()

    for item in data:
        if is_one_different(current, item):
            match = item
            break

    if match:
        break

letters_in_common = ''

for a, b in zip(current, match):
    if a == b:
        letters_in_common += a


print(letters_in_common)
