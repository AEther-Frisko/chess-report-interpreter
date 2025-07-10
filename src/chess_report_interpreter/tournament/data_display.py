"""Module for displaying data related to the Tournament."""

from .player import ChessPlayer
from .result import ResultEnum
from .tournament import ChessTournament


class DataDisplay:
    def display_leaderboard(top_players: list[tuple[int, float]], tournament: ChessTournament):
        """Displays the top three players of the tournament, according to their win/loss/draw scores."""
        
        print("--- TOP PLAYERS ---")
        for seed, score in top_players:
            player = tournament.get_player(seed)
            print(
                f"{top_players.index((seed, score)) + 1}.\n"
                f"Name:     {player.name}\n"
                f"Score:    {score}\n"
                "----------"
                )
    
    def display_player_report(results: list[tuple[ResultEnum, str]]):
        """Displays the player report for a specific player."""

        print("--- PLAYER TOURNAMENT RESULTS ---")
        round = 0
        for result, opponent in results:
            round += 1
            print(
                f"Round:    {round}\n"
                f"Opponent: {opponent}\n"
                f"Result:   {result}\n"
                "----------"
            )
    
    def display_player_brief(player: ChessPlayer):
        """Displays the basic player data, without the seed or round results."""

        print(
            f"Name:         {player.name}\n"
            f"CFC ID:       {player.cfc_id}\n"
            f"CFC Rating:   {player.cfc_rating}\n"
            "----------"
        )