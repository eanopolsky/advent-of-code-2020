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

containing_bags = set()
for bag_color in contain_rules.keys():
    if "shiny gold" in [contained_bag["color"] for contained_bag in contain_rules[bag_color]]:
        containing_bags.add(bag_color)

previous_size = len(containing_bags)
while True:
    for bag_color in contain_rules.keys():
        if containing_bags.intersection(set([contained_bag["color"] for contained_bag in contain_rules[bag_color]])):
            containing_bags.add(bag_color)
    if len(containing_bags) == previous_size:
        break
    else:
        previous_size = len(containing_bags)

print(len(containing_bags))
