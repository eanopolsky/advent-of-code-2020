#!/usr/bin/python3

import loader
import logging
import re

#logging.basicConfig(level=logging.DEBUG)

valid_passport_required_keys = ["byr",
                                "iyr",
                                "eyr",
                                "hgt",
                                "hcl",
                                "ecl",
                                "pid"]
                                #"cid"]

passport_string_list = loader.string_list("input_day4")

all_passports = []
current_passport = {}
for line in passport_string_list:
    logging.debug(f"Got line: {line}")
    if line == "":
        logging.debug(f"Found blank line. Added {current_passport} to all_passports")
        all_passports.append(current_passport)
        current_passport = {}
        continue
    else:
        field_data = line.split()
        for field in field_data:
            split_field = field.split(":")
            current_passport[split_field[0]] = split_field[1]

if len(current_passport.keys()) != 0:
    all_passports.append(current_passport) # file does not end with blank line
            


valid_passports = []
for passport in all_passports:
    if len(set(valid_passport_required_keys) - set(passport.keys())) != 0:
        logging.debug(f"Rejecting passport {passport} due to invalid field set.")
        continue
    valid_passports.append(passport)
    
print(f"Valid passports: {len(valid_passports)}")
                   

