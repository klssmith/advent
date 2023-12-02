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

possible_games = []


def is_game_possible(cube_draws):
    for item in cube_draws:
        if item["red"] > 12 or item["green"] > 13 or item["blue"] > 14:
            return False

    return True


for game_id, cube_draws in formatted_data.items():
    if is_game_possible(cube_draws):
        possible_games.append(int(game_id))

print(sum(possible_games))
