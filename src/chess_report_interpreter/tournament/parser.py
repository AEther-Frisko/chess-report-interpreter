"""Module for the file parsing superclass."""


class Parser:
    """The parent class for file parsers."""
    
    @staticmethod
    def read_file(filename: str):
        """Reads all the lines of a file and returns them as a list."""
        lines = list()
        try:
            file = open(filename)
            lines = file.readlines()
            file.close()
            return lines
        except FileNotFoundError:
            print("ERROR: This file does not exist or cannot be found.")