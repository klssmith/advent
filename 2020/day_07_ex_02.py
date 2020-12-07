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
            number, colour = re.match(
                re.compile(r"^ ?([0-9]) ([a-z]* [a-z]*) bag"), rough_colour
            ).group(1, 2)
            graph[node].append({colour: int(number)})

total_bags = 0


def count_contained_bags(parent):
    children = graph[parent]
    for child in children:
        for colour, quantity in child.items():
            global total_bags
            total_bags += quantity
            for i in range(quantity):
                count_contained_bags(colour)


count_contained_bags("shiny gold")

print(total_bags)
