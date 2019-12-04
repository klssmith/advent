#! /usr/bin/env python

import re

matcher = re.compile(r'^0*1*2*3*4*5*6*7*8*9*$')

start_no = 264360
end_no = 746325


possible_options = []
for i in range(start_no, end_no + 1):
    possible_options.append(str(i))


def fits_the_pattern(password):
    return matcher.match(password) and len(set(password)) <= 5


valid_passwords = filter(fits_the_pattern, possible_options)

print(len(list(valid_passwords)))
