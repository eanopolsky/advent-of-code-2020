#!/usr/bin/python3

import loader
import logging

#logging.basicConfig(level=logging.DEBUG)

tree_grid = loader.CharacterGrid("input_day3")
current_x = 0
current_y = 0
move_right = 3
move_down = 1
tree_count = 0

while True:
    logging.debug(f"Starting position: ({current_x}, {current_y})")
    current_x += move_right
    current_y += move_down
    logging.debug(f"After naive move: ({current_x}, {current_y})")
    current_x %= (tree_grid.get_max_x() + 1)
    logging.debug(f"After wrapping: ({current_x}, {current_y})")
    logging.debug(f"Found character: {tree_grid.get_character(current_x,current_y)}")
    if tree_grid.get_character(current_x,current_y) == "#":
        tree_count += 1
        tree_grid.set_character(current_x,current_y,"X")
    else:
        tree_grid.set_character(current_x,current_y,"O")
    if current_y == tree_grid.get_max_y():
        break

#tree_grid.display()
print(tree_count)
