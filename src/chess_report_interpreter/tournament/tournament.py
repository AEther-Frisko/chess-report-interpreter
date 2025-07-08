"""Tournament class for managing chess tournaments."""

from .player import ChessPlayer


class ChessTournament:
    """A class representing a chess tournament."""

    def __init__(self, name: str, organizer: str, date: str):
        """Initializes a ChessTournament instance."""
        self.name = name
        self.organizer = organizer
        self.date = date
        self.players: list[ChessPlayer] = []

    def __str__(self) -> str:
        """Returns a string representation of the ChessTournament."""
        players_str = "\n".join(str(player) for player in self.players)
        return (
            f"Tournament Name: {self.name}\n"
            f"Organizer:       {self.organizer}\n"
            f"Date:            {self.date}\n"
            f"Players:\n{players_str}"
        )

    def add_player(self, player: ChessPlayer):
        """Adds a player to the tournament."""
        if not isinstance(player, ChessPlayer):
            raise TypeError("Expected a ChessPlayer instance.")
        self.players.append(player)

    def get_player_list(self) -> list[ChessPlayer]:
        """Returns the list of players in the tournament."""
        return self.players

    def get_players_by_seed(self) -> list[ChessPlayer]:
        """Returns the list of players sorted by their seed number."""
        return sorted(self.players, key=lambda player: player.seed)

    def get_players_by_rating(self) -> list[ChessPlayer]:
        """Returns the list of players sorted by their CFC rating."""
        return sorted(self.players, key=lambda player: player.cfc_rating, reverse=True)

    def get_tournament_details(self) -> str:
        """Returns the tournament details as a formatted string."""
        return (
            f"Tournament: {self.name}\n"
            f"Organizer: {self.organizer}\n"
            f"Date: {self.date}\n"
        )