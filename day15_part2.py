#!/usr/bin/python3

import loader

inp = loader.string_list("input_day15")

number_list = [int(i) for i in inp[0].split(",")]

number_history = [None for i in range(30000000)]

for i in range(len(number_list)-1):
    number_history[number_list[i]] = i

last_said_number_index = len(number_list)-1
last_said_number = number_list[-1]

while True:
    previous_last_said_number_index = number_history[last_said_number]
    if previous_last_said_number_index == None:
        new_number = 0
    else:
        new_number = last_said_number_index - previous_last_said_number_index
    number_history[last_said_number] = last_said_number_index
    last_said_number = new_number
    last_said_number_index += 1
    if last_said_number_index == 30000000-1:
        print(last_said_number)
        break
