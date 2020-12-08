#!/usr/bin/python3

import loader
import copy

inp = loader.string_list("input_day8")

instructions = []
for line in inp:
    split_line = line.split(" ")
    opcode = split_line[0]
    argument = split_line[1]
    if argument[0] == "+":
        argument = argument[1:]
    instructions.append({"opcode": opcode,
                         "argument": int(argument),
                         "execution_count": 0})

original_machine_state = {"instructions": instructions,
                          "registers": { "acc": 0,
                                         "ip": 0 } }

def execute_one_instruction(machine_state):
    current_instruction = machine_state["instructions"][machine_state["registers"]["ip"]]
    if current_instruction["opcode"] == "acc":
        machine_state["registers"]["acc"] += current_instruction["argument"]
        current_instruction["execution_count"] += 1
        machine_state["registers"]["ip"] += 1
    elif current_instruction["opcode"] == "nop":
        current_instruction["execution_count"] += 1
        machine_state["registers"]["ip"] += 1
    elif current_instruction["opcode"] == "jmp":
        current_instruction["execution_count"] += 1
        machine_state["registers"]["ip"] += current_instruction["argument"]
    else:
        raise ValueError(f"Invalid opcode: {current_instruction['opcode']}")

def run_until_loop_or_halt(machine_state):
    while True:
        if machine_state["registers"]["ip"] == len(machine_state["instructions"]):
            print(f"Solution found: {machine_state['registers']['acc']}")
            exit(0)
        if machine_state["instructions"][machine_state["registers"]["ip"]]["execution_count"] != 0:
            return # loop detected
        execute_one_instruction(machine_state)

for i in range(len(original_machine_state["instructions"])):
    modified_machine_state = copy.deepcopy(original_machine_state)
    if modified_machine_state["instructions"][i]["opcode"] == "nop":
        modified_machine_state["instructions"][i]["opcode"] = "jmp"
    elif modified_machine_state["instructions"][i]["opcode"] == "jmp":
        modified_machine_state["instructions"][i]["opcode"] = "nop"
    else:
        continue
    run_until_loop_or_halt(modified_machine_state)

        
