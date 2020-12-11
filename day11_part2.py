#!/usr/bin/python3

from functools import lru_cache
import loader

inp = loader.CharacterGrid("input_day11")

@lru_cache(maxsize=None)
def get_visible_positions(x,y):
    """
    Returns a list of visible seats at a given coordinate in the initial input.
    """
    direction_vectors = [(-1,-1),
                         (-1,0),
                         (-1,1),
                         (0,-1),
                         (0,1),
                         (1,-1),
                         (1,0),
                         (1,1)]
    visible_positions = []
    for d in direction_vectors:
        for multiplier in range(1,max([inp.get_max_x(),
                                       inp.get_max_y()])):
            test_position = (x + (multiplier * d[0]),
                             y + (multiplier * d[1]))
            try:
                if inp.get_character(test_position[0],test_position[1]) == ".":
                    continue # get a new multiplier
                else:
                    visible_positions.append(test_position)
                    break # get a new direction vector
            except KeyError:
                break # no seats visible in this direction
    print(visible_positions)
    return visible_positions
    
    
def produce_next_step(current_seating):
    """
    Produces a character grid representing the next iteration according to the rules.
    """
    new_seating = current_seating.copy()
    for p in current_seating.get_occupied_positions():
        if current_seating.get_character(p[0],p[1]) == ".":
            continue
        visible_positions = get_visible_positions(p[0],p[1])
        occupied_adjacent_seats = 0
        for adjacent_position in visible_positions:
            try:
                if current_seating.get_character(adjacent_position[0],
                                                 adjacent_position[1]) == "#":
                    occupied_adjacent_seats += 1
            except KeyError:
                pass
        if occupied_adjacent_seats == 0 and current_seating.get_character(p[0],p[1]) == "L":
            new_seating.set_character(p[0],p[1],"#")
        elif occupied_adjacent_seats >= 5 and current_seating.get_character(p[0],p[1]) == "#":
            new_seating.set_character(p[0],p[1],"L")
    return new_seating

def count_occupied_seats(current_seating):
    occupied_seat_count = 0
    for p in current_seating.get_occupied_positions():
        if current_seating.get_character(p[0],p[1]) == "#":
            occupied_seat_count += 1
    return occupied_seat_count
            

old_seating = inp
new_seating = produce_next_step(old_seating)
iteration_count = 1
while new_seating != old_seating:
    old_seating = new_seating
    new_seating = produce_next_step(old_seating)
    iteration_count +=1
    print(f"Performed {iteration_count} new seating iterations.")
print(f"After {iteration_count} iterations, found {count_occupied_seats(new_seating)} seats occupied.")
