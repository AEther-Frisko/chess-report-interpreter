"""Module for compiling all player data for a tournament."""

from tournament.result import ResultEnum
from tournament.player import ChessPlayer


class ChessTournament:
    """A class representing all the results of a chess tournament."""

    def __init__(self, players: dict[int, ChessPlayer]):
        """Initializes a tournament instance."""
        self.players = players

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
            results.append((outcome, opponent.name))
        return results
