#! /usr/bin/env python

with open('/where_i_write_hacky_code/advent/day_13/input_file.txt') as f:
    data = f.read().strip().split('\n')

firewall = {}
for row in data:
    key = int(row.split(':')[0])
    num = int(row.split()[-1])
    numbers = [x for x in range(num)]
    firewall[key] = {
        'position': 0,
        'numbers': numbers,
        'down': True
    }


def move_scanner(layer):
    if layer['down']:
        if layer['position'] == layer['numbers'][-1]:
            layer['position'] -= 1
            layer['down'] = False
        else:
            layer['position'] += 1
    else:
        if layer['position'] == 0:
            layer['position'] += 1
            layer['down'] = True
        else:
            layer['position'] -= 1
    return layer


firewall_layers = max(firewall)
score = 0

for layer in range(firewall_layers + 1):
    if firewall.get(layer, {}).get('position') == 0:
        score += len(firewall[layer]['numbers']) * layer

    for key, value in firewall.items():
        firewall[key] = move_scanner(value)

print(score)
