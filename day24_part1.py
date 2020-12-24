#!/usr/bin/python3

import loader

inp = loader.string_list("input_day24")

def parse_direction_line(direction_line_text):
    directions = []
    i = 0
    while i < len(direction_line_text):
        if direction_line_text[i] in ('e','w'):
            directions.append(direction_line_text[i])
            i += 1
            continue
        elif direction_line_text[i:i+2] in ('nw','ne','sw','se'):
            directions.append(direction_line_text[i:i+2])
            i += 2
            continue
        else:
            raise RuntimeError(f"Error parsing line {direction_line_text} at offset {i}.")
    return directions

parsed_directions = [parse_direction_line(line) for line in inp]


def get_canonical_coordinates(direction_list):
    """
    Takes a direction list as produced by parse_direction_line.

    Returns a 2-tuple (x,y) where x and y are integers identifying a hexagon.
    x is the number of 'e' moves necessary and y is the number of 'ne' moves necessary to reach it.
    If x or y is negative, that means a corresponding number of 'w' and/or 'sw' moves are necessary to reach it.
    """
    x = 0
    y = 0
    for move in direction_list:
        if move == "e":
            x += 1
            continue
        elif move == "w":
            x -= 1
            continue
        elif move == "ne":
            y += 1
            continue
        elif move == "sw":
            y -= 1
            continue
        elif move == "nw":
            x -= 1
            y += 1
            continue
        elif move == "se":
            x += 1
            y -= 1
            continue
        else:
            raise ValueError(f"Unknown move {move}")
    return (x,y)

indicated_tiles_canonical_coordinates = [get_canonical_coordinates(direction_list) for direction_list in parsed_directions]

black_tiles = 0
for identified_tile_coords in set(indicated_tiles_canonical_coordinates):
    if len([coords for coords in indicated_tiles_canonical_coordinates if coords == identified_tile_coords]) % 2 == 0:
        continue
    else:
        black_tiles += 1

print(black_tiles)
