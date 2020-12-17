#!/usr/bin/python3

import loader
import copy

inp = loader.string_list("input_day17")

cube_state = {}

for x in range(len(inp[0])):
    for y in range(len(inp)):
        if inp[y][x] == "#":
            cube_state[(x,y,0)] = "active"

def get_bounds(some_cube_state):
    bounds = {}
    bounds["x_min"] = min([coords[0] for coords in some_cube_state])
    bounds["x_max"] = max([coords[0] for coords in some_cube_state])
    bounds["y_min"] = min([coords[1] for coords in some_cube_state])
    bounds["y_max"] = max([coords[1] for coords in some_cube_state])
    bounds["z_min"] = min([coords[2] for coords in some_cube_state])
    bounds["z_max"] = max([coords[2] for coords in some_cube_state])
    return bounds

def render_cube_state(some_cube_state):
    bounds = get_bounds(some_cube_state)
    for z in range(bounds["z_min"],bounds["z_max"]+1):
        print()
        print(f"z={z}")
        for y in range(bounds["y_min"],bounds["y_max"]+1):
            for x in range(bounds["x_min"],bounds["x_max"]+1):
                try:
                    coord_state = some_cube_state[(x,y,z)]
                except KeyError:
                    coord_state = "inactive"
                if coord_state == "active":
                    print("#",end="")
                elif coord_state == "inactive":
                    print(".",end="")
                else:
                    print("?",end="")
            print()

def get_neighbors(coord):
    neighbors = []
    for xdiff in (-1,0,1):
        for ydiff in (-1,0,1):
            for zdiff in (-1,0,1):
                if xdiff != 0 or ydiff != 0 or zdiff !=0:
                    neighbors.append((coord[0]+xdiff,coord[1]+ydiff,coord[2]+zdiff))
    return neighbors

def gen_next_cycle(original_cube_state):
    new_cube_state = copy.deepcopy(original_cube_state)
    bounds = get_bounds(original_cube_state)
    for z in range(bounds["z_min"]-1,bounds["z_max"]+2):
        for y in range(bounds["y_min"]-1,bounds["y_max"]+2):
            for x in range(bounds["x_min"]-1,bounds["x_max"]+2):
                neighbors = get_neighbors((x,y,z))
                active_neighbors = 0
                for neighbor in neighbors:
                    try:
                        if original_cube_state[neighbor] == "active":
                            active_neighbors += 1
                    except KeyError:
                        pass
                try:
                    original_state = original_cube_state[(x,y,z)]
                except KeyError:
                    original_state = "inactive"
                if original_state == "active" and active_neighbors not in (2,3):
                    new_cube_state[(x,y,z)] = "inactive"
                elif original_state == "inactive" and active_neighbors == 3:
                    new_cube_state[(x,y,z)] = "active"
    return new_cube_state


for i in range(6):
    #render_cube_state(cube_state)
    cube_state = gen_next_cycle(cube_state)
#render_cube_state(cube_state)
print(len([value for value in cube_state.values() if value == "active"]))
