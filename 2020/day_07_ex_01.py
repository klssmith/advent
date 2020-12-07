#! /usr/bin/env python

import re


with open("./data.txt") as f:
    data = [line.strip() for line in f.readlines()]


graph = {}

for line in data:
    node, description = line.split(" bags contain ")
    graph[node] = []
    if description != "no other bags.":
        colour_description = description.split(",")

        for rough_colour in colour_description:
            graph[node].append(
                re.match(
                    re.compile(r"^ ?[0-9] ([a-z]* [a-z]*) bag"), rough_colour
                ).group(1)
            )

node_results = set()


def get_parent_nodes(target):
    for node, node_children in graph.items():
        if target in node_children:
            node_results.add(node)
            get_parent_nodes(node)


get_parent_nodes("shiny gold")

print(len(node_results))
