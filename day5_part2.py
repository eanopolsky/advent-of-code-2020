#!/usr/bin/python3

import loader

boarding_passes = loader.string_list("input_day5")

def convert_pass_to_row_col(bpass):
    row = int(bpass[0:7].replace("F","0").replace("B","1"),2)
    col = int(bpass[7:].replace("L","0").replace("R","1"),2)
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

