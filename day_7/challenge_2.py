#! /usr/bin/env python

with open('/where_i_write_hacky_code/advent/day_7/input_file.txt') as f:
    data = f.read()

data = data.rstrip().split('\n')
nodes = {}

# this bit formats the data
for line in data:
    node_id = line.split()[0]
    nodes[node_id] = {}
    nodes[node_id]['weight'] = int(line.split()[1][1:-1])
    nodes[node_id]['children'] = []

    if '->' in line:
        words = line.split('->')[-1]
        words = words.split(',')
        for word in words:
            nodes[node_id]['children'].append(word.strip())


def get_weight_of_child_nodes(node):
    '''Recursively sums the given node and all nodes downstream'''
    if not node.get('children'):
        return node['weight']
    else:
        total = 0

        for child_id in node['children']:
            child_node = nodes.get(child_id)
            total += get_weight_of_child_nodes(child_node)
        return node['weight'] + total


start_node = nodes.get('mwzaxaj')  # this is the root node, found in part 1

for child_id in start_node['children']:
    child_node = nodes.get(child_id)
    branch_weight = get_weight_of_child_nodes(child_node)
    print('The weight of id {} is {}'.format(child_id, branch_weight))

# The rest of this needs to be calculated by hand ... 👋 📝
# First run the program using the id of the root node on line 36, then with each
# node that comes back that has a different value to the rest of the returned nodes.
# The first node that you reach that has all of its children balanced is the one
# with the dodgy weight. Compare its weight to the others at the same level to see
# what it should weigh, and you have the answer.
