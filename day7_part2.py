#!/usr/bin/python3

import loader
import re

inp = loader.string_list("input_day7")

contain_rules = {}
for line in inp:
    matches = re.match('^(.*) bags contain (.*)\.$',line)
    main_bag_color = matches.group(1)
    contained_bags_string = matches.group(2)
    contained_bags = []
    for contained_bag_string in contained_bags_string.split(", "):
        if contained_bag_string == "no other bags":
            break
        contained_bag_matches = re.match('^([0-9]+) (.*) bags?$',contained_bag_string)
        contained_bag = {"count": int(contained_bag_matches.group(1)),
                         "color": contained_bag_matches.group(2)}
        contained_bags.append(contained_bag)
    contain_rules[main_bag_color] = contained_bags

def count_bags_within(bag_color):
    if contain_rules[bag_color] == []:
        return 0
    bag_count = 0
    for sub_bag in contain_rules[bag_color]:
        bag_count += sub_bag["count"] * (count_bags_within(sub_bag["color"]) + 1)
    return bag_count

print(count_bags_within("shiny gold"))

