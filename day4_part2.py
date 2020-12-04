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
    if int(passport["byr"]) < 1920 or int(passport["byr"]) > 2002:
        logging.debug(f"Rejecting passport {passport} due to invalid byr.")
        continue
    if int(passport["iyr"]) < 2010 or int(passport["iyr"]) > 2020:
        logging.debug(f"Rejecting passport {passport} due to invalid iyr.")
        continue
    if int(passport["eyr"]) < 2020 or int(passport["eyr"]) > 2030:
        continue
    height_unit = passport["hgt"][-2:]
    height_number = int(passport["hgt"][:-2])
    if height_unit == "cm" and (height_number < 150 or height_number > 193):
        continue
    elif height_unit == "in" and (height_number < 59 or height_number > 76):
        continue
    elif height_unit not in ("in", "cm"):
        continue #invalid height unit
    if not re.match('^#[0-9a-f]{6,6}$',passport["hcl"]):
        continue
    if passport["ecl"] not in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"):
        continue
    if not re.match('^[0-9]{9,9}$',passport["pid"]):
        continue
    valid_passports.append(passport)
    
print(f"Valid passports: {len(valid_passports)}")
                   

