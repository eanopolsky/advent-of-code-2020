#!/usr/bin/python3

import loader
from copy import deepcopy

inp = loader.string_list("input_day23")

raw_labels = inp[0]

cup_linked_list_head = {}
empty_element_pointer = cup_linked_list_head
previous_element_pointer = cup_linked_list_head # not technically correct, but will be overwritten shortly
max_label = 1000000 


for i in raw_labels:
    empty_element_pointer["label"] = int(i)
    empty_element_pointer["next"] = {}
    previous_element_pointer = empty_element_pointer
    empty_element_pointer = empty_element_pointer["next"]
for i in range(max([int(i) for i in raw_labels])+1,max_label+1):
    empty_element_pointer["label"] = int(i)
    if int(i) != 10:
        empty_element_pointer["smaller_label"] = previous_element_pointer
    empty_element_pointer["next"] = {}
    previous_element_pointer = empty_element_pointer
    empty_element_pointer = empty_element_pointer["next"]

previous_element_pointer["next"] = cup_linked_list_head
max_label_pointer = previous_element_pointer

next_smaller_label_assignment_pointer = cup_linked_list_head
while True:
    target_label = next_smaller_label_assignment_pointer["label"] - 1
    if target_label == 0:
        next_smaller_label_assignment_pointer["smaller_label"] = max_label_pointer
    else:
        search_pointer = cup_linked_list_head
        while True:
            if search_pointer["label"] == target_label:
                break
            else:
                search_pointer = search_pointer["next"]
        next_smaller_label_assignment_pointer["smaller_label"] = search_pointer
    next_smaller_label_assignment_pointer = next_smaller_label_assignment_pointer["next"]
    while "smaller_label" in next_smaller_label_assignment_pointer:
        next_smaller_label_assignment_pointer = next_smaller_label_assignment_pointer["next"]
        if next_smaller_label_assignment_pointer["label"] == cup_linked_list_head["label"]:
            break
    if next_smaller_label_assignment_pointer["label"] == cup_linked_list_head["label"]:
        break

current_cup = cup_linked_list_head

def perform_one_move():
    global current_cup
    picked_up_cups_head = current_cup["next"]
    picked_up_cups_labels = [picked_up_cups_head["label"],
                             picked_up_cups_head["next"]["label"],
                             picked_up_cups_head["next"]["next"]["label"]]
    current_cup["next"] = current_cup["next"]["next"]["next"]["next"] # cut out the picked up cups
    destination_cup_pointer = current_cup["smaller_label"]
    while True:
        if destination_cup_pointer["label"] not in picked_up_cups_labels:
            break
        else:
            destination_cup_pointer = destination_cup_pointer["smaller_label"]
    cup_after_destination_cup = destination_cup_pointer["next"]
    destination_cup_pointer["next"] = picked_up_cups_head
    picked_up_cups_head["next"]["next"]["next"] = cup_after_destination_cup
    current_cup = current_cup["next"]

def render_cups():
    print("cups: ",end="")
    if cup_linked_list_head["label"] == current_cup["label"]:
        print(f"({cup_linked_list_head['label']}) ",end="")
    else:
        print(f"{cup_linked_list_head['label']} ",end="")
    printing_cup = cup_linked_list_head["next"]
    while True:
        if printing_cup == cup_linked_list_head:
            break
        if printing_cup["label"] == current_cup["label"]:
            print(f"({printing_cup['label']}) ",end="")
        else:
            print(f"{printing_cup['label']} ",end="")
        printing_cup = printing_cup["next"]
    print()

for i in range(10000000):
    perform_one_move()

search_pointer = cup_linked_list_head
while True:
    if search_pointer["label"] != 1:
        search_pointer = search_pointer["next"]
    else:
        break

print(search_pointer["next"]["label"]*search_pointer["next"]["next"]["label"])
