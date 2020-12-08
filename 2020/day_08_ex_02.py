#! /usr/bin/env python

with open("./data.txt") as f:
    data = f.readlines()


def get_accumulator_value(data):
    accumulator = 0
    current_index = 0
    seen_instruction_indexes = set()
    infinite_loop = False

    while True:
        # Reached the end of the file with no infinite loop
        if current_index == len(data):
            break

        current_instruction, number = data[current_index].split()
        number = int(number)

        current_index += number if current_instruction == "jmp" else 1
        accumulator += number if current_instruction == "acc" else 0

        if current_index in seen_instruction_indexes:
            infinite_loop = True
            break
        seen_instruction_indexes.add(current_index)

    return accumulator, infinite_loop


for i in range(len(data)):
    if (current_instruction := data[i].split()[0]) == "acc":
        continue
    elif current_instruction == "jmp":
        data_copy = data.copy()
        data_copy[i] = data_copy[i].replace("jmp", "nop")
        accumulator, infinite_loop = get_accumulator_value(data_copy)
    elif current_instruction == "nop":
        data_copy = data.copy()
        data_copy[i] = data_copy[i].replace("nop", "jmp")
        accumulator, infinite_loop = get_accumulator_value(data_copy)

    if not infinite_loop:
        print(accumulator)
