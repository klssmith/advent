#! /usr/bin/env python

with open("./data.txt") as f:
    group_data = f.read().split("\n\n")


print(
    sum(len(set.intersection(*[set(x) for x in group.split()])) for group in group_data)
)

# Or, to make it readable...

# total = 0
# for group in group_data:
#     answers_per_person = [set(x) for x in group.split()]
#     total += len(set.intersection(*answers_per_person))

# print(total)
