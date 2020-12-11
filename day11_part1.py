#!/usr/bin/python3

import loader

inp = loader.CharacterGrid("input_day11")

def produce_next_step(current_seating):
    """
    Produces a character grid representing the next iteration according to the rules.
    """
    new_seating = current_seating.copy()
    for p in current_seating.get_occupied_positions():
        if current_seating.get_character(p[0],p[1]) == ".":
            continue
        adjacent_positions = [(p[0]-1,p[1]-1),
                              (p[0]-1,p[1]),
                              (p[0]-1,p[1]+1),
                              (p[0],p[1]-1),
                              (p[0],p[1]+1),
                              (p[0]+1,p[1]-1),
                              (p[0]+1,p[1]),
                              (p[0]+1,p[1]+1)]
        occupied_adjacent_seats = 0
        for adjacent_position in adjacent_positions:
            try:
                if current_seating.get_character(adjacent_position[0],
                                                 adjacent_position[1]) == "#":
                    occupied_adjacent_seats += 1
            except KeyError:
                pass
        if occupied_adjacent_seats == 0 and current_seating.get_character(p[0],p[1]) == "L":
            new_seating.set_character(p[0],p[1],"#")
        elif occupied_adjacent_seats >= 4 and current_seating.get_character(p[0],p[1]) == "#":
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
print(f"After {iteration_count} iterations, found {count_occupied_seats(new_seating)} seats occupied.")
