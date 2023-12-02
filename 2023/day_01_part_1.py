#! /usr/bin/env python

import re

with open("./data.txt") as f:
    data = f.readlines()


numbers = [re.findall(r"[123456789]", line) for line in data]

first_and_last_numbers = [num[0] + num[-1] for num in numbers]

answer = sum([int(x) for x in first_and_last_numbers])

print(answer)
