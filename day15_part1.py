#!/usr/bin/python3

import loader

inp = loader.string_list("input_day15")

number_list = [int(i) for i in inp[0].split(",")]

while True:
    if len(number_list) == 2020:
        print(number_list[-1])
        break
    if number_list[-1] not in number_list[0:-1]:
        number_list.append(0)
        continue
    new_i = len(number_list)
    for old_i in range(len(number_list)-2,-1,-1):
        if number_list[old_i] == number_list[-1]:
            number_list.append(len(number_list)-1-old_i)
            break
