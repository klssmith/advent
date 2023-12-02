#! /usr/bin/env python

import re

with open("./data.txt") as f:
    data = f.readlines()


formatted_data = {}

for line in data:
    game_id = re.search(r"[\d]+", line)[0]
    all_games = []
    cubes = line.split(":")[1].strip().split(";")

    for item in cubes:
        red = re.search(r"[\d]+(?= red)", item)
        green = re.search(r"[\d]+(?= green)", item)
        blue = re.search(r"[\d]+(?= blue)", item)

        cube_dict = {}
        cube_dict["red"] = int(red[0]) if red else 0
        cube_dict["green"] = int(green[0]) if green else 0
        cube_dict["blue"] = int(blue[0]) if blue else 0

        all_games.append(cube_dict)

    formatted_data[game_id] = all_games


minimum_sets = []

for cube_data in formatted_data.values():
    red = max(x["red"] for x in cube_data)
    green = max(x["green"] for x in cube_data)
    blue = max(x["blue"] for x in cube_data)

    minimum_sets.append(red * green * blue)

print(sum(minimum_sets))
