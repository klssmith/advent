#! /usr/bin/env python

with open('./data.txt') as f:
    data = f.read().split()


def position(code, min_no, max_no, min_zone_marker):
    for c in code:
        if c == min_zone_marker:
            # The position is in the lower seat numbers
            max_no = (max_no - min_no) // 2 + min_no
        else:
            min_no = max_no - ((max_no - min_no) // 2)

    return min_no


print(max(
    position(seat_code[:-3], 0, 127, 'F') * 8 + position(seat_code[-3:], 0, 7, 'L')
    for seat_code in data
))
