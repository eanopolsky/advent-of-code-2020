#!/usr/bin/python3

import loader

inp = loader.integer_list("input_day25")

card_public_key = inp[0]
door_public_key = inp[1]

card_loop_size = 0
subject_number = 7
transformed_value = 7
while True:
    if transformed_value == card_public_key:
        break
    else:
        transformed_value = (transformed_value * subject_number) % 20201227
        card_loop_size += 1

door_loop_size = 0
transformed_value = 7
while True:
    if transformed_value == door_public_key:
        break
    else:
        transformed_value = (transformed_value * subject_number) % 20201227
        door_loop_size += 1

encryption_key = door_public_key
for i in range(card_loop_size):
    encryption_key = (encryption_key * door_public_key) % 20201227

print(encryption_key)
