#! /usr/bin/env python

with open("./data.txt") as f:
    data = [int(x) for x in f.readlines()]


def add_pairs_of_different_numbers(numbers):
    results = set()
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            if numbers[i] != numbers[j]:
                results.add(numbers[i] + numbers[j])

    return results


for i in range(25, len(data)):
    previous_numbers = data[i - 25 : i]

    if data[i] not in add_pairs_of_different_numbers(previous_numbers):
        print(data[i])
        break
