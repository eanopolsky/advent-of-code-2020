#!/usr/bin/python3

import loader

inp = loader.integer_list("input_day9")

def is_sum_of_two(candidate_list, target_number):
    """
    Determines whether target_number is the sum of two distinct elements of
    a list of numbers.

    Mandatory arguments:
    * candidate_list - a list of integers that may be added together.
    * target_number - the desired sum

    Returns True if target_number is the sum of two distinct elements of the
    list, or False otherwise.
    """
    for i in range(len(candidate_list)-1):
        for j in range(i+1,len(candidate_list)):
            if candidate_list[i] + candidate_list[j] == target_number:
                return True
    return False

invalid_number = 0
for i in range(25,len(inp)):
    candidate_list = inp[(i-25):i]
    target_number = inp[i]
    if not is_sum_of_two(candidate_list,target_number):
        invalid_number = target_number
        break

for run_length in range(2,len(inp)):
    for start_index in range(0,len(inp)-1):
        if sum(inp[start_index:(start_index+run_length)]) == invalid_number:
            smallest_number = min(inp[start_index:(start_index+run_length)])
            largest_number = max(inp[start_index:(start_index+run_length)])
            print(smallest_number + largest_number)
            exit(0)
