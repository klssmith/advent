#! /usr/bin/env python

steps = 343
buff = [0]
current_position = 0
value = 1

while value < 2018:
    if current_position + steps > len(buff):
        current_position = current_position + steps - len(buff)
    else:
        current_position += steps

    buff.insert(current_position + 1, value)
    current_position = buff.index(value)
    value += 1

position_of_2017 = buff.index(2017)
print(buff[position_of_2017 + 1])
