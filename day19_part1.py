#!/usr/bin/python3

import loader
import re

inp = loader.blank_line_delimited("input_day19")

raw_rules = inp[0]
raw_messages = inp[1]

rules = {}
for raw_rule in raw_rules:
    m = re.match(r'^(\d+): (.*)',raw_rule)
    rule_number = int(m.group(1))
    raw_definition = m.group(2)
    rules[rule_number] = raw_definition

def rule_to_regex(rule_number):
    if rules[rule_number] == '"a"':
        return "a"
    if rules[rule_number] == '"b"':
        return "b"
    if "|" not in rules[rule_number]:
        regex_text = ""
        for sub_rule in rules[rule_number].split(" "):
            regex_text += rule_to_regex(int(sub_rule))
        return regex_text
    # compound rule
    split_rule = rules[rule_number].split("|")
    lhs = split_rule[0].strip()
    rhs = split_rule[1].strip()
    regex_text = "("
    for sub_rule in lhs.split(" "):
        regex_text += rule_to_regex(int(sub_rule))
    regex_text += "|"
    for sub_rule in rhs.split(" "):
        regex_text += rule_to_regex(int(sub_rule))
    regex_text += ")"
    return regex_text

part1_regex = "^" + rule_to_regex(0) + "$"

match_count = 0
for message in raw_messages:
    if re.match(part1_regex,message):
        match_count += 1

print(match_count)
