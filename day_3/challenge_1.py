#! /usr/bin/env python

number = 312051
position = [0, 0]
counter = 1
repeat = 1
carry_on = True


def move_right():
    position[0] += 1


def move_up():
    position[1] += 1


def move_left():
    position[0] -= 1


def move_down():
    position[1] -= 1


while carry_on:
    for i in range(repeat):
        move_right()
        counter += 1
        if counter >= number:
            carry_on = False
            break

    if not carry_on:
        break

    for i in range(repeat):
        move_up()
        counter += 1
        if counter >= number:
            carry_on = False
            break

    if not carry_on:
        break

    repeat += 1

    for i in range(repeat):
        move_left()
        counter += 1
        if counter >= number:
            carry_on = False
            break

    if not carry_on:
        break

    for i in range(repeat):
        move_down()
        counter += 1
        if counter >= number:
            carry_on = False
            break

    if not carry_on:
        break

    repeat += 1

steps = abs(position[0]) + abs(position[1])
print(steps)
