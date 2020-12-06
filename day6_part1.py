#!/usr/bin/python3

import loader

inp = loader.string_list("input_day6")

groups = []
current_group = set()
for line in inp:
    if line == "":
        groups.append(current_group)
        current_group = set()
    else:
        for character in line:
            current_group.add(character)
groups.append(current_group)

print(sum([len(group) for group in groups]))
