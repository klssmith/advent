#! /usr/bin/env python

import re
from collections import Counter


ascending_digits = re.compile(r'^0*1*2*3*4*5*6*7*8*9*$')

start_no = 264360
end_no = 746325


possible_options = []
for i in range(start_no, end_no + 1):
    possible_options.append(str(i))


def has_a_digit_appearing_exactly_twice(password):
    counter = Counter(password)
    return 2 in counter.values()


def fits_the_pattern(password):
    return ascending_digits.match(password) and has_a_digit_appearing_exactly_twice(password)


valid_passwords = filter(fits_the_pattern, possible_options)

print(len(list(valid_passwords)))
