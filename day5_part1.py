#!/usr/bin/python3

import loader

boarding_passes = loader.string_list("input_day5")

def convert_pass_to_row_col(bpass):
    row = int(bpass[0:7].replace("F","0").replace("B","1"),2)
    col = int(bpass[7:].replace("L","0").replace("R","1"),2)
    return {"row": row,
            "col": col,
            "id": row * 8 + col }

print(max([convert_pass_to_row_col(bpass)["id"] for bpass in boarding_passes]))
