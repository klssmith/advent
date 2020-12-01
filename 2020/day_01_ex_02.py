#! /usr/bin/env python

with open('./data.txt') as f:
    data = f.readlines()


numbers = [int(line) for line in data]

for i in range(len(numbers)):
    sub_total = 2020 - numbers[i]

    for num in numbers[i:]:
        final_number = sub_total - num
        if final_number in numbers[i:]:
            a = numbers[i]
            b = num
            c = final_number


print(a * b * c)
