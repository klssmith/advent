#! /usr/bin/env python

with open("./data.txt") as f:
    data = [int(x) for x in f.readlines()]


sorted_adapters = sorted(data)
sorted_adapters.insert(0, 0)
sorted_adapters.append(max(data) + 3)

diffs = []

for i in range(len(sorted_adapters) - 1):
    diffs.append(sorted_adapters[i + 1] - sorted_adapters[i])

print(diffs.count(1) * diffs.count(3))
