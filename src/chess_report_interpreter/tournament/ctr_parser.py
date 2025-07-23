"""Module for reading ctr files and parsing the extracted data."""

from .parser import Parser


class ctrParser(Parser):
    """A class handling the parsing of ctr files and their data."""

    @staticmethod
    def parse_tournament_data(line: str):
        """Converts a proper comma-delimted line into tournament information."""
        # cleaning up the raw line
        line = line.replace('"', "")
        line = line.replace("\n", "")

        data = line.split(",")
        if len(data) == 10:
            return data
        else:
            print("Improper tournament data format.")
            return None
