#!/usr/bin/python3

import loader
import re

def parse_password_line(password_line):
    """
    Mandatory arguments:
    * password_line - a line taken directly from day 2's input.
      Example: "5-11 t: glhbttzvzttkdx"

    Returns:
    {"minimum": 5,
     "maximum": 11,
     "letter": "t",
     "password": "glhbttzvzttkdx"
    }
    """
    matches = re.match('^([0-9]+)-([0-9]+) (.): (.+$)', password_line)
    return {"minimum": int(matches.group(1)),
            "maximum": int(matches.group(2)),
            "letter": matches.group(3),
            "password": matches.group(4) }

def is_password_valid(password_dict):
    """
    Mandatory arguments:
    * password_dict - a password dictionary a returned by parse_password_line

    Returns True if the password is valid and False if it is not.
    """
    letter_count = sum([1 for letter in password_dict["password"]
                        if letter == password_dict["letter"] ])
    if password_dict["minimum"] <= letter_count <= password_dict["maximum"]:
        return True
    else:
        return False

password_lines = loader.string_list("input_day2")
password_dicts = [parse_password_line(password_line) for password_line in password_lines]
valid_password_count = sum([ 1 for password_dict in password_dicts if is_password_valid(password_dict) ])
print(valid_password_count)
