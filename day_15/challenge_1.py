#! /usr/bin/env python

a_value = 116
b_value = 299

a_factor = 16807
b_factor = 48271

divider = 2147483647

score = 0

for i in range(40000000):
    a_value = (a_value * a_factor) % divider
    b_value = (b_value * b_factor) % divider

    a_binary = format(a_value, '032b')
    b_binary = format(b_value, '032b')

    if a_binary[16:] == b_binary[16:]:
        score += 1

print(score)
