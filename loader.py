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
