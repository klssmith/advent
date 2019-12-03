#! /usr/bin/env python

with open('./data.txt') as f:
    data = f.readlines()


wire_1 = data[0].strip().split(',')
wire_2 = data[1].strip().split(',')


def get_points_passed(wire_data):
    points_passed = {}
    current_point = [0, 0]
    total_steps = 0

    for instruction in wire_data:
        steps = int(instruction[1:])

        if (direction := instruction[0]) == 'R':
            for i in range(steps):
                total_steps += 1
                current_point[0] += 1
                if tuple(current_point) not in points_passed:
                    points_passed[tuple(current_point)] = total_steps
        elif direction == 'U':
            for i in range(steps):
                total_steps += 1
                current_point[1] += 1
                if tuple(current_point) not in points_passed:
                    points_passed[tuple(current_point)] = total_steps
        elif direction == 'L':
            for i in range(steps):
                total_steps += 1
                current_point[0] -= 1
                if tuple(current_point) not in points_passed:
                    points_passed[tuple(current_point)] = total_steps
        elif direction == 'D':
            for i in range(steps):
                total_steps += 1
                current_point[1] -= 1
                if tuple(current_point) not in points_passed:
                    points_passed[tuple(current_point)] = total_steps

    return points_passed


wire_1_points_passed = get_points_passed(wire_1)
wire_2_points_passed = get_points_passed(wire_2)
intersection_points = wire_1_points_passed.keys() & wire_2_points_passed.keys()

result = min([
    wire_1_points_passed[coordinate] + wire_2_points_passed[coordinate]
    for coordinate in intersection_points
])

print(result)
