#!/usr/bin/python3

import loader

inp = loader.string_list("input_day12")

inpp = [{'cmd': line[0], 'arg': int(line[1:])} for line in inp]

position = (0,0)

direction = (1,0)

def process_command(cmdd):
    global position
    global direction

    if cmdd["arg"] == 270:
        if cmdd["cmd"] == "R":
            cmdd["cmd"] = "L"
            cmdd["arg"] = 90
        elif cmdd["cmd"] == "L":
            cmdd["cmd"] = "R"
            cmdd["arg"] = 90

    if cmdd["cmd"] == "N":
        position = (position[0],position[1]+cmdd["arg"])
    elif cmdd["cmd"] == "S":
        position = (position[0],position[1]-cmdd["arg"])
    elif cmdd["cmd"] == "E":
        position = (position[0]+cmdd["arg"],position[1])
    elif cmdd["cmd"] == "W":
        position = (position[0]-cmdd["arg"],position[1])
    elif cmdd["cmd"] == "F":
        position = (position[0]+cmdd["arg"]*direction[0],
                    position[1]+cmdd["arg"]*direction[1])
    elif cmdd["cmd"] == "R":
        if cmdd["arg"] == 90:
            direction = (direction[1],-direction[0])
        elif cmdd["arg"] == 180:
            direction = (direction[0] * -1, direction[1] * -1)
    elif cmdd["cmd"] == "L":
        if cmdd["arg"] == 90:
            direction = (-direction[1],direction[0])
        elif cmdd["arg"] == 180:
            direction = (direction[0] * -1, direction[1] * -1)
    
for cmdd in inpp:
    process_command(cmdd)

print(abs(position[0])+abs(position[1]))
