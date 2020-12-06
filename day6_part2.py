#!/usr/bin/python3

import loader

inp = loader.string_list("input_day6")

groups = []
current_group = []
for line in inp:
    if line == "":
        groups.append(current_group)
        current_group = []
    else:
        current_group.append(set(line))
groups.append(current_group)

groups2 = []
for group in groups:
    common = group[0]
    for member in group:
        common = common.intersection(member)
    groups2.append(common)
    
print(sum([len(group) for group in groups2]))
