#!/usr/bin/python3

import loader
from functools import reduce

inp = loader.blank_line_delimited("input_day20")

tiles = {}
for raw_tile in inp:
    tile_id = int(raw_tile[0][5:9])
    tile_characters = {}
    for y in range(10):
        for x in range(10):
            tile_characters[(x,y)] = raw_tile[1+y][x]
    top_edge_binary_string = reduce(lambda x,y: x+y,[tile_characters[(x,0)] for x in range(10)]).replace(".","0").replace("#","1")
    right_edge_binary_string = reduce(lambda x,y: x+y,[tile_characters[(9,y)] for y in range(10)]).replace(".","0").replace("#","1")
    bottom_edge_binary_string = reduce(lambda x,y: x+y,[tile_characters[(9-x,9)] for x in range(10)]).replace(".","0").replace("#","1")
    left_edge_binary_string = reduce(lambda x,y: x+y,[tile_characters[(0,9-y)] for y in range(10)]).replace(".","0").replace("#","1")

    tiles[tile_id] = {}
    tiles[tile_id]["chars"] = tile_characters
    tiles[tile_id]["edge_numbers"] = {"top": int(top_edge_binary_string,2),
                                      "top_reverse": int(top_edge_binary_string[::-1],2),
                                      "right": int(right_edge_binary_string,2),
                                      "right_reverse": int(right_edge_binary_string[::-1],2),
                                      "bottom": int(bottom_edge_binary_string,2),
                                      "bottom_reverse": int(bottom_edge_binary_string[::-1],2),
                                      "left": int(left_edge_binary_string,2),
                                      "left_reverse": int(left_edge_binary_string[::-1],2)}


corner_tile_ids = []
shared_edge_summary = {}
for tile_id in tiles:
    other_tile_edge_numbers = []
    for other_tile_id in tiles:
        if other_tile_id == tile_id:
            continue
        else:
            other_tile_edge_numbers += tiles[other_tile_id]["edge_numbers"].values()
    shared_edges = 0
    if tiles[tile_id]["edge_numbers"]["top"] in other_tile_edge_numbers or \
       tiles[tile_id]["edge_numbers"]["top_reverse"] in other_tile_edge_numbers:
        shared_edges += 1
    if tiles[tile_id]["edge_numbers"]["right"] in other_tile_edge_numbers or \
       tiles[tile_id]["edge_numbers"]["right_reverse"] in other_tile_edge_numbers:
        shared_edges += 1
    if tiles[tile_id]["edge_numbers"]["bottom"] in other_tile_edge_numbers or \
       tiles[tile_id]["edge_numbers"]["bottom_reverse"] in other_tile_edge_numbers:
        shared_edges += 1
    if tiles[tile_id]["edge_numbers"]["left"] in other_tile_edge_numbers or \
       tiles[tile_id]["edge_numbers"]["left_reverse"] in other_tile_edge_numbers:
        shared_edges += 1
    try:
        shared_edge_summary[shared_edges] += 1
    except KeyError:
        shared_edge_summary[shared_edges] = 1
    if shared_edges == 2:
        corner_tile_ids.append(tile_id)

print(reduce(lambda x,y: x*y,corner_tile_ids))
