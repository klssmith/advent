#! /usr/bin/env python

with open("./data.txt") as f:
    data = f.readlines()


accumulator = 0
current_index = 0
seen_instruction_indexes = set()

while True:
    current_instruction, number = data[current_index].split()
    number = int(number)

    current_index += number if current_instruction == "jmp" else 1
    accumulator += number if current_instruction == "acc" else 0

    if current_index in seen_instruction_indexes:
        break
    seen_instruction_indexes.add(current_index)

print(accumulator)
