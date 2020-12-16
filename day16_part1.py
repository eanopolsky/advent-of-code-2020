#!/usr/bin/python3

import loader
import re

inp = loader.blank_line_delimited("input_day16")

raw_validation_rules = inp[0]
raw_my_ticket = inp[1]
raw_nearby_tickets = inp[2]

validation_rules = {}
for raw_rule in raw_validation_rules:
    match = re.match('^([^:]+): ([0-9]+)-([0-9]+) or ([0-9]+)-([0-9]+)',raw_rule)
    field_name = match.group(1)
    low1 = int(match.group(2))
    high1 = int(match.group(3))
    low2 = int(match.group(4))
    high2 = int(match.group(5))
    validation_rules[field_name] = {"low1": low1,
                                    "high1": high1,
                                    "low2": low2,
                                    "high2": high2}

nearby_tickets = []
for raw_nearby_ticket in raw_nearby_tickets:
    if raw_nearby_ticket == "nearby tickets:":
        continue
    else:
        nearby_tickets.append([int(value) for value in raw_nearby_ticket.split(",")])


def is_value_valid_for_any_field(test_value):
    for field_name in validation_rules:
        if validation_rules[field_name]["low1"] <= test_value <= validation_rules[field_name]["high1"]:
            return True
        elif validation_rules[field_name]["low2"] <= test_value <= validation_rules[field_name]["high2"]:
            return True
    return False

invalid_value_sum = 0
for ticket in nearby_tickets:
    for value in ticket:
        if not is_value_valid_for_any_field(value):
            invalid_value_sum += value

print(invalid_value_sum)
