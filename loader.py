"""
A library for loading AoC input files.
"""

def string_list(input_filename):
    """
    Returns a puzzle input as a list of strings, one per line. Newlines are
    stripped, but nothing else is.

    Mandatory arguments:
    * input_filename - the name of the input file relative to the current 
      directory.
    """
    with open(input_filename, "r") as f:
        return [line.rstrip('\n') for line in f.readlines()]

def integer_list(input_filename):
    """
    Returns a puzzle input as a list of integers, one per line.

    Mandatory arguments:
    * input_filename - the name of the input file relative to the current
      directory.
    """
    return [int(line) for line in string_list(input_filename)]
