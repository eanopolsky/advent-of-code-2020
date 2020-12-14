#!/usr/bin/python3

import loader
import re

inp = loader.string_list("input_day14")

mask = ""
mem = {}

for line in inp:
    #print()
    #print(f"line: {line}")
    if re.match('^mask',line):
        mask = line.split(" = ")[1]
        continue
    match = re.match('mem\[([0-9]+)] = ([0-9]+)',line)
    raw_mem_addr = int(match.group(1))
    value = int(match.group(2))
    raw_mem_addr_binary_string = "{:036b}".format(raw_mem_addr)
    float_mem_addr_string = ""
    for i in range(36):
        if mask[i] == "0":
            float_mem_addr_string += raw_mem_addr_binary_string[i]
        else:
            float_mem_addr_string += mask[i]
    split_mem_addr_string = float_mem_addr_string.split("X")
    floating_bits = len(split_mem_addr_string) - 1
    for float_set in range(2 ** floating_bits):
        format_string = "{:0" + str(floating_bits) + "b}"
        merge_bit_string = format_string.format(float_set)
        masked_addr = ""
        for i in range(len(split_mem_addr_string)):
            masked_addr += split_mem_addr_string[i]
            try:
                masked_addr += merge_bit_string[i]
            except IndexError:
                pass
        masked_addr_int = int(masked_addr,2)
        mem[masked_addr_int] = value

print(sum([mem[key] for key in mem.keys()]))
