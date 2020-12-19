#!/usr/bin/python3

import loader
import re
from functools import lru_cache

inp = loader.blank_line_delimited("input_day19")

raw_rules = inp[0]
raw_messages = inp[1]

rules = {}
for raw_rule in raw_rules:
    m = re.match(r'^(\d+): (.*)',raw_rule)
    rule_number = int(m.group(1))
    raw_definition = m.group(2)
    rules[rule_number] = raw_definition


#part 2 modifications:
rules[8] = "42 | 42 8"
rules[11] = "42 31 | 42 11 31"

@lru_cache(maxsize=None)
def rule_to_regex(rule_number):
    if rule_number == 8:
        return "(" + rule_to_regex(42) + ")+"
    if rule_number == 11:
        max_message_length = max([len(message) for message in raw_messages])
        regex_text = "("
        for i in range(1,max_message_length // 2):
            regex_text += rule_to_regex(42) * i + rule_to_regex(31) * i + "|"
        regex_text = regex_text[0:-1] + ")"
        return regex_text
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

regex_text = "^" + rule_to_regex(0) + "$"
compiled_regex = re.compile(regex_text)

match_count = 0
for message in raw_messages:
    if compiled_regex.match(message):
        match_count += 1

print(match_count)
