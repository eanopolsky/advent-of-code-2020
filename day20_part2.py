#!/usr/bin/python3

import loader
from functools import reduce
import copy

#inp = loader.string_list("input_day20")
#inp = loader.integer_list("input_day20")
inp = loader.blank_line_delimited("input_day20")
#inp = loader.CharacterGrid("input_day20")

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
    if shared_edges == 2:
        corner_tile_ids.append(tile_id)

top_left_id = corner_tile_ids[0]

def rotate_tile_id_90_clockwise(tile_id):
    new_characters = {}
    for location in tiles[tile_id]["chars"].keys():
        new_location = (9-location[1],location[0])
        new_characters[new_location] = tiles[tile_id]["chars"][location]
    new_edge_numbers = {}
    new_edge_numbers["right"] = tiles[tile_id]["edge_numbers"]["top"]
    new_edge_numbers["right_reverse"] = tiles[tile_id]["edge_numbers"]["top_reverse"]
    new_edge_numbers["bottom"] = tiles[tile_id]["edge_numbers"]["right"]
    new_edge_numbers["bottom_reverse"] = tiles[tile_id]["edge_numbers"]["right_reverse"]
    new_edge_numbers["left"] = tiles[tile_id]["edge_numbers"]["bottom"]
    new_edge_numbers["left_reverse"] = tiles[tile_id]["edge_numbers"]["bottom_reverse"]
    new_edge_numbers["top"] = tiles[tile_id]["edge_numbers"]["left"]
    new_edge_numbers["top_reverse"] = tiles[tile_id]["edge_numbers"]["left_reverse"]
    tiles[tile_id]["chars"] = new_characters
    tiles[tile_id]["edge_numbers"] = new_edge_numbers

def flip_tile_horizontally(tile_id):
    """
    Draws a line from the top edge to the bottom edge and flips around that line.
    The left side of the tile becomes the right and the right becomes the left.
    """
    new_characters = {}
    for location in tiles[tile_id]["chars"].keys():
        new_location = (9-location[0],location[1])
        new_characters[new_location] = tiles[tile_id]["chars"][location]
    new_edge_numbers = {}
    new_edge_numbers["top"] = tiles[tile_id]["edge_numbers"]["top_reverse"]
    new_edge_numbers["top_reverse"] = tiles[tile_id]["edge_numbers"]["top"]
    new_edge_numbers["bottom"] = tiles[tile_id]["edge_numbers"]["bottom_reverse"]
    new_edge_numbers["bottom_reverse"] = tiles[tile_id]["edge_numbers"]["bottom"]
    new_edge_numbers["left"] = tiles[tile_id]["edge_numbers"]["right_reverse"]
    new_edge_numbers["left_reverse"] = tiles[tile_id]["edge_numbers"]["right"]
    new_edge_numbers["right"] = tiles[tile_id]["edge_numbers"]["left_reverse"]
    new_edge_numbers["right_reverse"] = tiles[tile_id]["edge_numbers"]["left"]
    tiles[tile_id]["chars"] = new_characters
    tiles[tile_id]["edge_numbers"] = new_edge_numbers

def permute_tile(tile_id):
    #print(f"permuting tile ID {tile_id}")
    try:
        permute_count = tiles[tile_id]["permute_count"]
    except KeyError:
        tiles[tile_id]["permute_count"] = 0
    if tiles[tile_id]["permute_count"] <= 2:
        rotate_tile_id_90_clockwise(tile_id)
        tiles[tile_id]["permute_count"] += 1
        return
    elif tiles[tile_id]["permute_count"] == 3:
        flip_tile_horizontally(tile_id)
        tiles[tile_id]["permute_count"] += 1
        return
    elif 4 <= tiles[tile_id]["permute_count"] <= 6:
        rotate_tile_id_90_clockwise(tile_id)
        tiles[tile_id]["permute_count"] += 1
        return
    else:
        rotate_tile_id_90_clockwise(tile_id)
        tiles[tile_id]["permute_count"] = 0

arranged_tiles = {} # Keys are locations in tile slot space. Values are tile objects.

for tile_slot_y in range(12):
    for tile_slot_x in range(12):
        if tile_slot_x == 0 and tile_slot_y == 0:
            other_tile_edge_numbers = []
            for other_tile_id in tiles:
                if other_tile_id == top_left_id:
                    continue
                else:
                    other_tile_edge_numbers += tiles[other_tile_id]["edge_numbers"].values()
            while not ((tiles[top_left_id]["edge_numbers"]["right"] in other_tile_edge_numbers or \
                        tiles[top_left_id]["edge_numbers"]["right_reverse"] in other_tile_edge_numbers) and \
                       (tiles[top_left_id]["edge_numbers"]["bottom"] in other_tile_edge_numbers or \
                        tiles[top_left_id]["edge_numbers"]["bottom_reverse"] in other_tile_edge_numbers)):

                permute_tile(top_left_id)
            #print("finished orienting top left tile")
            arranged_tiles[(tile_slot_x,tile_slot_y)] = tiles.pop(top_left_id)
        elif tile_slot_y == 0:
            left_neighbor_edge_number_right = arranged_tiles[(tile_slot_x-1,tile_slot_y)]["edge_numbers"]["right"]
            for other_tile in tiles:
                for i in range(8):
                    if tiles[other_tile]["edge_numbers"]["left_reverse"] == left_neighbor_edge_number_right:
                        break
                    else:
                        permute_tile(other_tile)
                if tiles[other_tile]["edge_numbers"]["left_reverse"] != left_neighbor_edge_number_right:
                    continue #try another tile
                else:
                    #found the correctly oriented neighbor
                    arranged_tiles[(tile_slot_x,tile_slot_y)] = tiles.pop(other_tile)
                    break
        else: # top row is finished
            upper_neighbor_edge_number_bottom = arranged_tiles[(tile_slot_x,tile_slot_y-1)]["edge_numbers"]["bottom"]
            for other_tile in tiles:
                for i in range(8):
                    if tiles[other_tile]["edge_numbers"]["top_reverse"] == upper_neighbor_edge_number_bottom:
                        break
                    else:
                        permute_tile(other_tile)
                if tiles[other_tile]["edge_numbers"]["top_reverse"] != upper_neighbor_edge_number_bottom:
                    continue
                else:
                    arranged_tiles[(tile_slot_x,tile_slot_y)] = tiles.pop(other_tile)
                    break

#print(len(tiles))
#print(len(arranged_tiles))
                
large_map = {}
for y in range(8*12):
    for x in range(8*12):
        tile_slot_x = x // 8
        tile_slot_y = y // 8
        x_offset = x % 8 + 1
        y_offset = y % 8 + 1
        large_map[(x,y)] = arranged_tiles[(tile_slot_x,tile_slot_y)]["chars"][(x_offset,y_offset)]

def render_large_map():
    for y in range(8*12):
        for x in range(8*12):
            print(large_map[(x,y)],end='')
        print()

#render_large_map()

def is_sea_monster_at(location):
    """
    Location is an (x,y) tuple specifying the upper left corner of a potential sea monster pattern.
    Sea monster pattern is 20 characters wide by 3 characters tall:
    .#...#.###...#.##.O#
    O.##.OO#.#.OO.##.OOO
    #O.#O#.O##O..O.#O##.
    """
    sea_monster_hash_offsets = [(0,1),(1,2),
                                (4,2),(5,1),(6,1),(7,2),
                                (10,2),(11,1),(12,1),(13,2),
                                (16,2),(17,1),(18,0),(18,1),(19,1)]
    x = location[0]
    y = location[1]
    hashes_found = len([hash_offset for hash_offset in sea_monster_hash_offsets if large_map[(x+hash_offset[0],y+hash_offset[1])] == "#"])
    if hashes_found == 15:
        return True
    else:
        return False

def rotate_large_map_90_clockwise():
    global large_map
    new_large_map = {}
    for location in large_map:
        if not isinstance(location,tuple):
            new_large_map[location] = large_map[location]
            continue
        new_location = (8*12-1-location[1],location[0])
        new_large_map[new_location] = large_map[location]
    large_map = new_large_map

def flip_large_map_horizontally():
    global large_map
    new_large_map = {}
    for location in large_map:
        if not isinstance(location,tuple):
            new_large_map[location] = large_map[location]
            continue
        new_location = (8*12-1-location[0],location[1])
        new_large_map[new_location] = large_map[location]
    large_map = new_large_map


def permute_large_map():
    try:
        permute_count = large_map["permute_count"]
    except KeyError:
        large_map["permute_count"] = 0
    if large_map["permute_count"] <= 2:
        rotate_large_map_90_clockwise()
        large_map["permute_count"] += 1
        return
    elif large_map["permute_count"] == 3:
        flip_large_map_horizontally()
        large_map["permute_count"] += 1
        return
    elif 4 <= large_map["permute_count"] <= 6:
        rotate_large_map_90_clockwise()
        large_map["permute_count"] += 1
        return
    else:
        rotate_large_map_90_clockwise()
        large_map["permute_count"] = 0

def count_sea_monsters():
    sea_monster_count = 0
    for y in range(8*12-2):
        for x in range(8*12-19):
            if is_sea_monster_at((x,y)):
                sea_monster_count += 1
    return sea_monster_count

while count_sea_monsters() == 0:
    permute_large_map()

sea_monster_hashes = count_sea_monsters()*15

total_hashes = len([location for location in large_map if large_map[location] == "#"])

print(total_hashes - sea_monster_hashes)
