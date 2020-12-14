#!/usr/bin/python3

import loader
import re

inp = loader.string_list("input_day14")

mask = ""
mem = {}
for line in inp:
    if re.match('^mask',line):
        mask = line.split(" = ")[1]
        continue
    match = re.match('mem\[([0-9]+)] = ([0-9]+)',line)
    mem_addr = int(match.group(1))
    raw_value = int(match.group(2))
    raw_value_binary_string = "{:036b}".format(raw_value)
    masked_value_binary_string = ""
    for i in range(36):
        if mask[i] != "X":
            masked_value_binary_string += mask[i]
        else:
            masked_value_binary_string += raw_value_binary_string[i]
    masked_value_int = int(masked_value_binary_string,2)
    mem[mem_addr] = masked_value_int

print(sum([mem[key] for key in mem.keys()]))
