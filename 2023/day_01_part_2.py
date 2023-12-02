#! /usr/bin/env python

import re

with open("./data.txt") as f:
    data = f.readlines()


def add_digit(word):
    replacement = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    while number_found := re.search(r"one|two|three|four|five|six|seven|eight|nine", word):
        word = (
            word[: number_found.start()]
            + replacement[number_found[0]]
            + word[number_found.start() + 1 :]
        )

    return word


digits_added = [add_digit(x) for x in data]
numbers = [re.findall(r"[123456789]", line) for line in digits_added]
first_and_last_numbers = [num[0] + num[-1] for num in numbers]

answer = sum([int(x) for x in first_and_last_numbers])

print(answer)
