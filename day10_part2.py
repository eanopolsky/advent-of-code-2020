#!/usr/bin/python3

import loader
import itertools

inp = loader.integer_list("input_day10")

inp.append(0) # include the wall outlet
inp.append(max(inp)+3) # include the device

inp.sort()

# jolt_differences = {1: 0,
#                     2: 0,
#                     3: 0}

# for i in range(len(inp)-1):
#     jolt_differences[inp[i+1]-inp[i]] += 1

# jolt_differences[inp[0]] += 1 #accounting for the charging outlet difference
# jolt_differences[3] += 1 #accounting for the device difference
# print(jolt_differences[1]*jolt_differences[3])

def is_valid_combination(adapter_list):
    """
    Determines whether a given set of adapters can be successfully connected
    together.

    Mandatory arguments:
    * adapter_list - a sorted iterable of integers specifying adapter joltages.
    
    Returns True if the list can be connected without exceeding a 3 joltage 
    difference between adjacent adapters or False otherwise.
    """
    for i in range(len(adapter_list)-1):
        if (adapter_list[i+1] - adapter_list[i]) > 3:
            return False
    return True

def count_valid_combinations(adapter_list):
    """
    Returns the number of valid adapter combinations that bridge the lowest
    joltage adapter to the highest.
    
    Mandatory arguments:
    * adapter_list - a *sorted* list of integers specifying adapter joltages
                     for which there is at least one valid connection
                     combination.

    Returns an integer with the total number of ways to connect the lowest 
    joltage adapter to the highest.
    """
    if len(adapter_list) < 3:
        return 1
    lowest = adapter_list[0]
    highest = adapter_list[-1]
    middle = adapter_list[1:-1]

    valid_combinations = 0
    for subset_size in range(len(middle)+1):
        for subset in itertools.combinations(middle,subset_size):
            subset_list = list(subset)
            subset_list.append(lowest)
            subset_list.append(highest)
            subset_list.sort()
            if is_valid_combination(subset_list):
                valid_combinations += 1
    return valid_combinations

adapter_chain_start_indices = [0]
for i in range(len(inp)-1):
    if (inp[i+1] - inp[i]) == 3:
        adapter_chain_start_indices.append(i+1)

adapter_chains = []
for i in range(len(adapter_chain_start_indices)-1):
    slice_start = adapter_chain_start_indices[i]
    slice_end = adapter_chain_start_indices[i+1]
    adapter_chains.append(inp[slice_start:slice_end])

final_slice_start = adapter_chain_start_indices[-1]
adapter_chains.append(inp[final_slice_start:])

valid_combinations = 1
for adapter_chain in adapter_chains:
    valid_combinations *= count_valid_combinations(adapter_chain)
print(valid_combinations)



    
    
