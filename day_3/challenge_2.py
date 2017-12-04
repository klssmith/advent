#! /usr/bin/env python

number = 312051
position = [0, 0]
cell_value = 1
repeat = 1
values = {(0, 0): 1}
carry_on = True


def move_right():
    position[0] += 1


def move_up():
    position[1] += 1


def move_left():
    position[0] -= 1


def move_down():
    position[1] -= 1


def get_cell_value():
    x = position[0]
    y = position[1]

    right = values.get((x + 1, y), 0)
    top_right = values.get((x + 1, y + 1), 0)
    top = values.get((x, y + 1), 0)
    top_left = values.get((x - 1, y + 1), 0)
    left = values.get((x - 1, y), 0)
    bottom_left = values.get((x - 1, y - 1), 0)
    bottom = values.get((x, y - 1), 0)
    bottom_right = values.get((x + 1, y - 1), 0)

    return (right + top_right + top + top_left + left + bottom_left + bottom
            + bottom_right)


while carry_on:
    for i in range(repeat):
        move_right()
        cell_value = get_cell_value()
        values[(position[0], position[1])] = cell_value
        if cell_value > number:
            carry_on = False
            break

    if not carry_on:
        break

    for i in range(repeat):
        move_up()
        cell_value = get_cell_value()
        values[(position[0], position[1])] = cell_value
        if cell_value > number:
            carry_on = False
            break

    if not carry_on:
        break

    repeat += 1

    for i in range(repeat):
        move_left()
        cell_value = get_cell_value()
        values[(position[0], position[1])] = cell_value
        if cell_value > number:
            carry_on = False
            break

    if not carry_on:
        break

    for i in range(repeat):
        move_down()
        cell_value = get_cell_value()
        values[(position[0], position[1])] = cell_value
        if cell_value > number:
            carry_on = False
            break

    if not carry_on:
        break

    repeat += 1

print(cell_value)
