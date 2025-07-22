"""Module for analyzing and displaying the details of a ChessTournament."""

from enum import Enum
from .tournament import ChessTournament


class PointValueEnum(Enum):
    """An enumeration representing the point values of the potential results of a chess game."""

    WIN = 1.0
    LOSS = 0.0
    DRAW = 0.5

    @classmethod
    def from_result(cls, result: str):
        """Converts a chess result into a point value."""
        mapping = {"W": cls.WIN.value, "L": cls.LOSS.value, "D": cls.DRAW.value}
        return mapping.get(result.upper(), 0.0)


class TournamentAnalyzer:
    """Class for analyzing tournament data."""

    def get_top_three(data: ChessTournament):
        """Determines and orders the top three players in the tournament data."""

        scores: dict[int, float] = {}

        for player in data.players:
            score = 0
            for res in data.players[player].results:
                # convert result into points and add to score
                score += PointValueEnum.from_result(res.result)
            
            # create a dict entry with the player seed and score
            scores[data.players[player].seed] = score
        
        # order the list from highest to lowest, taking only the top three
        top_players = sorted(scores.items(), key = lambda x: x[1], reverse = True)[:3]
        return top_players