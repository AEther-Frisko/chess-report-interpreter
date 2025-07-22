"""Module for reading tms files and parsing the extracted data."""

from .result import ChessResult
from .player import ChessPlayer


class tmsParser:
    """A class handling the parsing of tms files and their data."""

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
        

    @staticmethod
    def parse_lines(lines: list[str]):
        """Converts a list of lines into a dictionary of Players."""
        players: dict[int, ChessPlayer] = {}
        for line in lines:
            data = line.split("	")
            seed = int(data[0])
            name = data[1]
            cfcID = int(data[2])
            cfcRating = int(data[3])
            results = data[4:]
            del results[-1]
            
            # converts into typical ChessResult format if using Round Robin.
            for res in results:
                if res[0] in {"1", "=", "0"}:
                    mapping = {"1": "W", "0": "L", "=":"D"}
                    result = mapping.get(res[0])
                    vs_seed = results.index(res) + 1
                    results[results.index(res)] = result + str(vs_seed)

            parsed_results = [ChessResult(res) for res in results]

            p = ChessPlayer(seed, name, cfcID, cfcRating, parsed_results)
            players[p.seed] = p
        return players
