#! /usr/bin/env python

with open('./data.txt') as f:
    data = f.readlines()


wire_1 = data[0].strip().split(',')
wire_2 = data[1].strip().split(',')


def get_points_passed(wire_data):
    points_passed = set()
    current_point = [0, 0]

    for instruction in wire_data:
        steps = int(instruction[1:])

        if (direction := instruction[0]) == 'R':
            for i in range(steps):
                current_point[0] += 1
                points_passed.add(tuple(current_point))
        elif direction == 'U':
            for i in range(steps):
                current_point[1] += 1
                points_passed.add(tuple(current_point))
        elif direction == 'L':
            for i in range(steps):
                current_point[0] -= 1
                points_passed.add(tuple(current_point))
        elif direction == 'D':
            for i in range(steps):
                current_point[1] -= 1
                points_passed.add(tuple(current_point))

    return points_passed


intersection_points = get_points_passed(wire_1) & get_points_passed(wire_2)

result = min([
        (abs(coordinate[0]) + abs(coordinate[1]))
        for coordinate in intersection_points
    ])

print(result)
