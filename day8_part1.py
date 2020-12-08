#!/usr/bin/python3

import loader

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

machine_state = {"instructions": instructions,
                 "registers": { "acc": 0,
                                "ip": 0}
                 }

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

while True:
    if machine_state["instructions"][machine_state["registers"]["ip"]]["execution_count"] != 0:
        print(machine_state["registers"]["acc"])
        exit(0)
    execute_one_instruction(machine_state)

