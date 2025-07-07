"""Module for compiling all player data for a tournament."""

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
                return player.name
            else:
                return "Not Found"
