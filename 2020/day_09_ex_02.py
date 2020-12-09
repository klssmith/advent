#! /usr/bin/env python

with open("./data.txt") as f:
    data = [int(x) for x in f.readlines()]

target = 1639024365
start_index = 0

for i in range(len(data)):
    list_to_add = []
    total = 0
    index_of_number_to_add = i

    while total < target:
        list_to_add.append(data[index_of_number_to_add])
        index_of_number_to_add += 1
        total = sum(list_to_add)

    if total == target:
        print(min(list_to_add) + max(list_to_add))
        break
