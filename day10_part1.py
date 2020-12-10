#!/usr/bin/python3

import loader

inp = loader.integer_list("input_day10")

inp.sort()

jolt_differences = {1: 0,
                    2: 0,
                    3: 0}

for i in range(len(inp)-1):
    jolt_differences[inp[i+1]-inp[i]] += 1

jolt_differences[inp[0]] += 1 #accounting for the charging outlet difference
jolt_differences[3] += 1 #accounting for the device difference
print(jolt_differences[1]*jolt_differences[3])

                     
