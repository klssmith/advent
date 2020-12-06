#! /usr/bin/env python

with open("./data.txt") as f:
    group_data = f.read().split("\n\n")

print(sum(len(set(group.replace("\n", ""))) for group in group_data))
