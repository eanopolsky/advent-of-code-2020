"""
A library for loading AoC input files.
"""

import logging

logger = logging.getLogger(__name__)


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

def blank_line_delimited(input_filename):
    """
    Parses puzzle input in blank line delimited format.

    Blank line delimited format files are ASCII text files consisting of blank
    lines (i.e. lines consisting only of a newline character) and non-blank 
    lines. Adjacent non-blank lines are logically grouped together in some way
    by the problem description.

    Puzzles using this input format include days 4 and 6. As of this writing
    (day 6), the final group has never been terminated by a blank line.

    Mandatory arguments:
    * input_filename - the name of the input file relative to the current
      directory.

    Returns a list of lists of strings. Elements of the top level list represent
    groups of adjacent, related lines. Those elements are lists of strings, with
    each string containing a single line of text (sans newline).
    """
    raw_string_list = string_list(input_filename)
    top_level_list = []
    group_being_built = []
    for line in raw_string_list:
        if line != "":
            group_being_built.append(line)
            continue
        else:
            top_level_list.append(group_being_built)
            group_being_built = []
    if group_being_built == []:
        logger.warning("The final group ended with a blank line. This loader may not be appropriate for this input.")
        return top_level_list
    else:
        top_level_list.append(group_being_built)
        return top_level_list

class CharacterGrid:
    """
    Represents a puzzle input as a grid of characters.

    The first character in the file is at position (0,0). The positive x axis 
    extends to the right, and the positive y axis extends download. For example,
    the fifth character on the 2nd line would be at position (1,4).
    """
    def __init__(self,input_filename):
        """
        Loads the puzzle input data.

        Mandatory arguments:
        * input_filename - the name of the input file relative to the current
          directory.
        """
        input_as_string_list = string_list(input_filename)
        self.__character_positions = {}
        for y in range(len(input_as_string_list)):
            for x in range(len(input_as_string_list[y])):
                self.__character_positions[(x,y)] = {"character": input_as_string_list[y][x]}
    def get_character(self, x, y):
        """
        Retrieves a single character in a given position.

        Mandatory arguments:
        * x - the x coordinate (i.e. column starting from 0) of the desired 
              character.
        * y - the y coordinate (i.e. line starting from 0) of the desired 
              character.
        """
        return self.__character_positions[(x,y)]["character"]

    def set_character(self, x, y, new_character):
        """
        Sets the character at position (x,y) to new_character.
        """
        try:
            self.__character_positions[(x,y)]["character"] = new_character
        except KeyError:
            self.__character_positions[(x,y)] = {"character": new_character}
            logger.debug(f"Setting character at position ({x},{y}). There was no character previously at this location.")
    def set_highlight(self, x, y):
        """
        Causes the character at the given position to be highlighted in an ANSI 
        terminal when display() is called.
        """
        try:
            self.__character_positions[(x,y)]["highlighted"] = True
        except KeyError:
            logger.error(f"Attempted to highlight nonexistent character at position ({x},{y}).")
            raise
    def clear_highlight(self, x, y):
        """
        Causes the character at the given position to be printed without ANSI
        color when display() is called.
        """
        try:
            self.__character_positions[(x,y)]["highlighted"] = False
        except KeyError:
            logger.error(f"Attempted to clear highlight on nonexistent character at position ({x},{y}).")
            raise
    def get_max_x(self):
        """
        Retrieves the largest x coordinate occupied by a character.
        """
        return max([position_tuple[0] for position_tuple in self.__character_positions.keys()])

    def get_max_y(self):
        """
        Retrieves the largest y coordinate occupied by a character.
        """
        return max([position_tuple[1] for position_tuple in self.__character_positions.keys()])
    def display(self):
        """
        Prints the character grid to the console.
        """
        x = 0
        y = 0
        while True:
            try:
                character_position = self.__character_positions[(x,y)]
                try:
                    highlighted = character_position["highlighted"]
                except:
                    highlighted = False
                if highlighted:
                    print('\033[41m' + character_position["character"] + '\033[49m', end='')
                else:
                    print(character_position["character"], end='')
            except KeyError:
                if x == 0:
                    break
                else:
                    y += 1
                    x = 0
                    print('')
                    continue
            x += 1
