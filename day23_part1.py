#!/usr/bin/python3

import loader
from copy import deepcopy

inp = loader.string_list("input_day23")
raw_labels = inp[0] #production

game_state = {}
cup_state = list()
for i in raw_labels:
    cup_state.append(int(i))

game_state["cup_state"] = cup_state
game_state["current_cup_offset"] = 0

def perform_one_move(old_game_state):
    new_game_state = deepcopy(old_game_state)
    old_current_cup_label = new_game_state["cup_state"][new_game_state["current_cup_offset"]]
    taken_cups = list()
    for take_offset in range(1,4):
        take_index = (new_game_state["current_cup_offset"]+take_offset) % len(new_game_state["cup_state"])
        taken_cups.append(new_game_state["cup_state"][take_index])
    take_offset_start = (new_game_state["current_cup_offset"] + 1) % len(new_game_state["cup_state"])
    if ((len(new_game_state["cup_state"])-1) - take_offset_start) >= 2:
        new_game_state["cup_state"].pop(take_offset_start)
        new_game_state["cup_state"].pop(take_offset_start)
        new_game_state["cup_state"].pop(take_offset_start)
    elif ((len(new_game_state["cup_state"])-1) - take_offset_start) == 1:
        new_game_state["cup_state"].pop(take_offset_start)
        new_game_state["cup_state"].pop(take_offset_start)
        new_game_state["cup_state"].pop(0)
    elif ((len(new_game_state["cup_state"])-1) - take_offset_start) == 0:
        new_game_state["cup_state"].pop(take_offset_start)
        new_game_state["cup_state"].pop(0)
        new_game_state["cup_state"].pop(0)
    else:
        raise RuntimeError("This should never happen.")
    destination_cup_label = 0
    for candidate_destination_cup in list(range(old_current_cup_label-1,0,-1))+list(range(9,old_current_cup_label,-1)):
        if candidate_destination_cup in new_game_state["cup_state"]:
            destination_cup_label = candidate_destination_cup
            break
    destination_cup_index = 0
    for i in range(len(new_game_state["cup_state"])):
        if new_game_state["cup_state"][i] == destination_cup_label:
            destination_cup_index = i
            break
    taken_cups.reverse()
    for taken_cup in taken_cups:
        new_game_state["cup_state"].insert(destination_cup_index+1,taken_cup)
    old_current_cup_index = 0
    for i in range(len(new_game_state["cup_state"])):
        if new_game_state["cup_state"][i] == old_current_cup_label:
            new_game_state["current_cup_offset"] = (i + 1) % len(new_game_state["cup_state"])
            break
    return new_game_state

def render_game_state(game_state):
    print("cups: ",end="")
    for i in range(len(game_state["cup_state"])):
        if i == game_state["current_cup_offset"]:
            print(f"({game_state['cup_state'][i]}) ",end="")
        else:
            print(f"{game_state['cup_state'][i]} ",end="")
    print()

for i in range(100):
    game_state = perform_one_move(game_state)

one_index = game_state["cup_state"].index(1)
print("".join([str(element) for element in game_state["cup_state"][one_index+1:]+game_state["cup_state"][0:one_index]]))
