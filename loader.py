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
        self.character_positions = {}
        for y in range(len(input_as_string_list)):
            for x in range(len(input_as_string_list[y])):
                self.character_positions[(x,y)] = input_as_string_list[y][x]
    def get_character(self, x, y):
        """
        Retrieves a single character in a given position.

        Mandatory arguments:
        * x - the x coordinate (i.e. column starting from 0) of the desired 
              character.
        * y - the y coordinate (i.e. line starting from 0) of the desired 
              character.
        """
        return self.character_positions[(x,y)]

    def set_character(self, x, y, new_character):
        """
        Sets the character at position (x,y) to new_character.
        """
        self.character_positions[(x,y)] = new_character
    def get_max_x(self):
        """
        Retrieves the largest x coordinate occupied by a character.
        """
        return max([position_tuple[0] for position_tuple in self.character_positions.keys()])

    def get_max_y(self):
        """
        Retrieves the largest y coordinate occupied by a character.
        """
        return max([position_tuple[1] for position_tuple in self.character_positions.keys()])
    def display(self):
        """
        Prints the character grid to the console.
        """
        x = 0
        y = 0
        while True:
            try:
                print(self.get_character(x,y), end='')
            except KeyError:
                if x == 0:
                    break
                else:
                    y += 1
                    x = 0
                    print('')
                    continue
            x += 1
