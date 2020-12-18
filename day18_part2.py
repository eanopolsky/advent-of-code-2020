#!/usr/bin/python3

import loader
import re

inp = loader.string_list("input_day18")

def parse_expression(raw_string):
    if raw_string == "":
        return list()
    m = re.match(r'^ *([0-9]+|\+|\*|\(|\))(.*)',raw_string)
    try:
        first_item = int(m.group(1))
    except:
        first_item = m.group(1)
    parsed_expression = [first_item] + parse_expression(m.group(2))
    return parsed_expression

def evaluate_simple_expression(parsed_expression):    
    """
    Evaluates parsed expressions that do not contain parentheses. Returns a
    single integer.
    """
    if len(parsed_expression) == 1:
        return parsed_expression[0]
    if "+" not in parsed_expression:
        value = parsed_expression[0]
        remaining_expression = parsed_expression[1:]
        while len(remaining_expression) != 0:
            value *= remaining_expression[1]
            remaining_expression = remaining_expression[2:]
        return value
    for i in range(len(parsed_expression)):
        if parsed_expression[i] != "+":
            continue
        single_sum = parsed_expression[i-1] + parsed_expression[i+1]
        simpler_expression = parsed_expression[0:i-1] + [single_sum] + \
            parsed_expression[i+2:]
        return evaluate_simple_expression(simpler_expression)
    

def evaluate_complex_expression(parsed_expression):
    if len(parsed_expression) == 1:
        return parsed_expression[0]
    if "(" not in parsed_expression:
        return evaluate_simple_expression(parsed_expression)
    open_paren_index = 0 # necessary to declare ahead of time?
    close_paren_index = 0
    for i in range(len(parsed_expression)):
        if parsed_expression[i] == "(":
            open_paren_index = i
            continue
        if parsed_expression[i] == ")":
            close_paren_index = i
            break
    simpler_expression = parsed_expression[0:open_paren_index] + \
        [evaluate_simple_expression(parsed_expression[open_paren_index+1:close_paren_index])] + \
        parsed_expression[close_paren_index + 1:]
    return evaluate_complex_expression(simpler_expression)

expression_sum = 0
for expression in inp:
    expression_sum += evaluate_complex_expression(parse_expression(expression))
print(expression_sum)
