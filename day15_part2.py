#!/usr/bin/python3

import loader

inp = loader.string_list("input_day15")

number_list = [int(i) for i in inp[0].split(",")]

number_history = {}

def generate_new_number(number_history, last_said_number, last_said_number_index):
    """
    Returns the next number spoken.
    """
    if last_said_number not in number_history.keys():
        return 0
    else:
        return last_said_number_index - number_history[last_said_number]

for i in range(len(number_list)-1):
    number_history[number_list[i]] = i

last_said_number_index = len(number_list)-1
last_said_number = number_list[-1]

while True:
    new_number = generate_new_number(number_history, last_said_number, last_said_number_index)
    number_history[last_said_number] = last_said_number_index
    last_said_number = new_number
    last_said_number_index += 1
    if last_said_number_index == 30000000-1:
        print(last_said_number)
        break
    
