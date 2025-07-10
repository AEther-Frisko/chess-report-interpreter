"""Module for compiling all player data for a tournament."""

from .result import ResultEnum
from .player import ChessPlayer


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

    def display_report(self, seed: int):
        """Displays a report of a player's tournament results."""
        player = self.get_player(seed)
        round = 0
        for result in player.results:
            round += 1
            outcome = ResultEnum.from_code(result.result)
            opponent = self.get_player(result.vs_seed)
            print(
                f"Round:    {round}\n"
                f"Opponent: {opponent.name}\n"
                f"Result:   {outcome}\n"
                "----------\n"
            )
