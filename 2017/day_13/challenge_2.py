#! /usr/bin/env python

with open('/where_i_write_hacky_code/advent/day_13/input_file.txt') as f:
    data = f.read().strip().split('\n')

firewall = {}
for row in data:
    key, value = [int(x) for x in row.split(': ')]
    firewall[key] = value


def is_at_top(time, scanner_range):
    return time % (2 * scanner_range - 2) == 0


delay = 0
firewall_layers = max(firewall)
success = False

while not success:
    time = delay
    success = True

    for layer in range(firewall_layers + 1):
        if firewall.get(layer) and is_at_top(time, firewall[layer]):
            success = False
            break
        time += 1
    delay += 1

print(delay - 1)
