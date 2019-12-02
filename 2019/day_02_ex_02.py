#! /usr/bin/env python

with open('./data.txt') as f:
    data = [int(i) for i in f.read().split(',')]


def calculate_position_0_value(data):
    for i in range(0, len(data), 4):
        if data[i] == 1:
            position_1 = data[i + 1]
            position_2 = data[i + 2]
            position_3 = data[i + 3]
            data[position_3] = data[position_1] + data[position_2]
        elif data[i] == 2:
            position_1 = data[i + 1]
            position_2 = data[i + 2]
            position_3 = data[i + 3]
            data[position_3] = data[position_1] * data[position_2]
        elif data[i] == 99:
            break

    return data[0]


required_answer = 19690720
correct_noun = None
correct_verb = None


for noun in range(100):
    for verb in range(100):
        copied_data = data.copy()
        copied_data[1] = noun
        copied_data[2] = verb

        result = calculate_position_0_value(copied_data)

        if result == required_answer:
            correct_verb = verb
            break

    if correct_verb:
        correct_noun = noun
        break


print(100 * correct_noun + correct_verb)
