"""Module for compiling all tournament data."""

from enum import Enum
from .result import ResultEnum
from .player import ChessPlayer


class PairingEnum(Enum):
    """An enumeration representing possible pairing styles in a tournament."""

    SWISS = "Swiss"
    RR = "Round Robin"

    @classmethod
    def from_code(cls, code: str):
        """Converts a single character to the corresponding PairingEnum."""
        mapping = {"S": cls.SWISS, "R": cls.RR}
        return mapping.get(code)
    
    def __str__(self):
        return self.value


class FormatEnum(Enum):
    """An enumeration representing possible formats of a tournament."""

    ACTIVE = "Active"
    REGULAR = "Regular"

    @classmethod
    def from_code(cls, code: str):
        """Converts a single character to the corresponding FormatEnum."""
        mapping = {"A": cls.ACTIVE, "R": cls.REGULAR}
        return mapping.get(code)
    
    def __str__(self):
        return self.value


class ChessTournament:
    """A class representing all the results of a chess tournament."""

    def __init__(self, players: dict[int, ChessPlayer], data: list[str] | None):
        """Initializes a tournament instance."""
        self.players = players
        
        if data is not None:
            self.info = {
                "Event": data[0],
                "Province": data[1],
                "Reference Number": data[2],
                "Pairings": PairingEnum.from_code(data[3]).value,
                "End Date": data[4],
                "Player Total": int(data[5]),
                "Round Total": int(data[6]),
                "Format": FormatEnum.from_code(data[7]).value,
                "Organizer": int(data[8]),
                "Arbiter": int(data[9])
            }

    def get_player(self, seed: int):
        """Returns a Player via the seed value."""
        return self.players.get(seed)

    def get_player_by_name(self, name: str):
        """Returns a Player via the name value."""
        for player in self.players.values():
            if player.name.lower() == name.lower():
                return player
        return None
    
    def create_report(self, seed: int):
        """Creates a report of a player's tournament results."""
        results: list[tuple[ResultEnum, str]] = []
        player = self.get_player(seed)
        for result in player.results:
            outcome = ResultEnum.from_code(result.result)
            opponent = self.get_player(result.vs_seed)
            if opponent is not None:
                results.append((outcome, opponent.name))
            else:
                results.append((outcome, "NA"))
        return results
