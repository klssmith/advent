#! /usr/bin/env python

with open("./data.txt") as f:
    data = [int(x) for x in f.readlines()]


sorted_adapters = sorted(data)
target = max(sorted_adapters) + 3
sorted_adapters.insert(0, 0)
sorted_adapters.append(target)


cache = {}

for index, adapter in reversed(list(enumerate(sorted_adapters))):
    if adapter == target:
        cache[target] = 1
    else:
        steps_from_this_adapter = (
            cache.get(adapter + 1, 0)
            + cache.get(adapter + 2, 0)
            + cache.get(adapter + 3, 0)
        )
        cache[adapter] = steps_from_this_adapter

print(cache[0])
