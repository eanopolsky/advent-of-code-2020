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

my_ticket = [int(value) for value in raw_my_ticket[1].split(",")]

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

valid_tickets = []
for ticket in nearby_tickets:
    validation_results = [is_value_valid_for_any_field(value) for value in ticket]
    if False in validation_results:
        continue
    else:
        valid_tickets.append(ticket)

def can_offset_be_field_name(offset,field_name):
    values_at_offset = [ticket[offset] for ticket in valid_tickets]
    for value in values_at_offset:
        if not (validation_rules[field_name]["low1"] <= value <= validation_rules[field_name]["high1"]) and \
           not (validation_rules[field_name]["low2"] <= value <= validation_rules[field_name]["high2"]):
            return False
    return True

field_name_to_offset_map = {}
while len(field_name_to_offset_map) < len(validation_rules):
    for field_name in validation_rules:
        if field_name in field_name_to_offset_map:
            continue
        unidentified_offsets = [offset for offset in range(len(valid_tickets[0])) if offset not in field_name_to_offset_map.values()]
        offset_assessment = [offset for offset in unidentified_offsets if can_offset_be_field_name(offset,field_name)]
        if len(offset_assessment) == 1:
            field_name_to_offset_map[field_name] = offset_assessment[0]
        else:
            continue

interesting_field_names = [field_name for field_name in validation_rules if re.match('^departure',field_name)]
output_product = 1
for field_name in interesting_field_names:
    output_product *= my_ticket[field_name_to_offset_map[field_name]]
print(output_product)
