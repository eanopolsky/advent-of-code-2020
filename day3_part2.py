#!/usr/bin/python3

import loader
import logging
from functools import reduce

#logging.basicConfig(level=logging.DEBUG)

tree_grid = loader.CharacterGrid("input_day3")

def count_trees(move_right, move_down):
    """
    Returns the number of trees encountered using the defined slope.
    """
    tree_count = 0
    current_x = 0
    current_y = 0
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
        if current_y == tree_grid.get_max_y():
            break
    return tree_count

puzzle_slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
trees_encountered = [count_trees(puzzle_slope[0],puzzle_slope[1]) for puzzle_slope in puzzle_slopes]
print(reduce((lambda x, y: x * y),trees_encountered))
