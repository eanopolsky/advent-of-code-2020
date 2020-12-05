#!/usr/bin/python3

import loader

boarding_passes = loader.string_list("input_day5")

def convert_pass_to_row_col(bpass):
    row = 0
    col = 0
    if bpass[0] == "B":
        row += 64
    if bpass[1] == "B":
        row += 32
    if bpass[2] == "B":
        row += 16
    if bpass[3] == "B":
        row += 8
    if bpass[4] == "B":
        row += 4
    if bpass[5] == "B":
        row += 2
    if bpass[6] == "B":
        row += 1
    if bpass[7] == "R":
        col += 4
    if bpass[8] == "R":
        col += 2
    if bpass[9] == "R":
        col += 1
    return {"row": row,
            "col": col,
            "id": row * 8 + col }

seat_ids = [convert_pass_to_row_col(bpass)["id"] for bpass in boarding_passes]
min_id = min(seat_ids)
max_id = max(seat_ids)

for seat_id in range(min_id,max_id):
    if seat_id not in seat_ids:
        print(seat_id)

