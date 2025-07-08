"""The player module defines individual players in a chess tournament."""

from src.chess_report_interpreter.tournament.result import ChessTournamentResult


class ChessPlayer:
    """A class representing a player in a chess tournament."""

    def __init__(
        self,
        seed_no: int,
        name: str,
        cfc_id: int,
        cfc_rating: int,
        results: list[ChessTournamentResult],
    ):
        """Initializes a Player instance."""
        self.seed = seed_no
        self.name = name
        self.cfc_id = cfc_id
        self.cfc_rating = cfc_rating
        self.results = results

    def __str__(self) -> str:
        results_str = "\n  ".join(str(result) for result in self.results)
        return (
            f"Seed:       {self.seed}\n"
            f"Name:       {self.name}\n"
            f"CFC ID:     {self.cfc_id}\n"
            f"CFC Rating: {self.cfc_rating}\n"
            f"Results:\n  {results_str}\n"
        )
    
    def get_player_details(self) -> str:
        """Returns the player's details as a formatted string."""
        return (
            f"Seed: {self.seed}, Name: {self.name}, CFC ID: {self.cfc_id}, "
            f"CFC Rating: {self.cfc_rating}"
        )

    def get_player_results(self) -> list[ChessTournamentResult]:
        """Returns the player's results."""
        output = ""
        for result in self.results:
            if result.vs_seed is not None:
                output += f"{result.get_short_result()} "
        return output
