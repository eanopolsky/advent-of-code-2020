#!/usr/bin/python3

import loader

boarding_passes = loader.string_list("input_day5")

def convert_pass_to_row_col(bpass):
    row = 0
    col = 0
    for i in range(7):
        if bpass[i] == "B":
            row += 2 ** (6-i)
    for i in range(3):
        if bpass[i+7] == "R":
            col += 2 ** (2-i)
    return {"row": row,
            "col": col,
            "id": row * 8 + col }

seat_ids = [convert_pass_to_row_col(bpass)["id"] for bpass in boarding_passes]
min_id = min(seat_ids)
max_id = max(seat_ids)

for seat_id in range(min_id,max_id):
    if seat_id not in seat_ids:
        print(seat_id)
        exit(0)

