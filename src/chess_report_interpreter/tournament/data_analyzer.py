"""Module for analyzing and displaying the details of a ChessTournament."""

from enum import Enum

from .result import ChessResult
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

    def calculate_score(results: list[ChessResult]):
        score = 0.0
        for res in results:
            score += PointValueEnum.from_result(res.result)
        return score

    @classmethod
    def get_top_three(cls, data: ChessTournament):
        """Determines and orders the top three players in the tournament data."""

        scores: dict[int, float] = {}

        for player in data.players:
            score = cls.calculate_score(data.players[player].results)
            
            # create a dict entry with the player seed and score
            scores[data.players[player].seed] = score
        
        # order the list from highest to lowest, taking only the top three
        top_players = sorted(scores.items(), key = lambda x: x[1], reverse = True)[:3]
        return top_players

    @classmethod
    def get_top_under_rating(cls, data: ChessTournament, max_rating: int):
        """Determines the top-scoring player within a certain rating threshold."""
        
        highest = {
            "Score": -1.0,
            "Player": None,
            "Max Rating": max_rating
        }
        for player in data.players:
            if data.players[player].cfc_rating < int(max_rating):
                score = cls.calculate_score(data.players[player].results)
                if score > highest["Score"]:
                    highest["Score"] = score
                    highest["Player"] = data.players[player]
        
        return highest