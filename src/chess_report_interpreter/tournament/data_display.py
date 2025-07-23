"""Module for displaying data related to the Tournament."""

from .data_analyzer import PointValueEnum
from .player import ChessPlayer
from .result import ResultEnum
from .tournament import ChessTournament


class DataDisplay:
    """Class for printing chess data to the terminal."""

    def display_leaderboard(top_players: list[tuple[int, float]], tournament: ChessTournament):
        """Displays the top three players of the tournament, according to their win/loss/draw scores."""
        
        print("--- TOP 3 PLAYERS ---")
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
    
    def display_round_overview(tournament: ChessTournament):
        """Displays an overview of all games in the tournament as a crosstable."""

        print("--- ROUND OVERVIEW ---")
        players = list(tournament.players.values())
        players.sort(key = lambda p: p.seed)

        round_num = max(len(p.results) for p in players)
        print(f"{'Player':<20} " + "  ".join(f"R{i+1}" for i in range(round_num)) + "  Total")
        print("----------")

        for player in players:
            row = f"{str(player.seed):<2} {player.name:<17}"
            score = 0.0
            for result in player.results:
                if result.result is None or result.vs_seed is None:
                    cell = "NA"
                else:
                    cell = f"{result.result}{result.vs_seed}"
                    score += float(PointValueEnum.from_result(result.result))
                row += f"{cell:^6}"
            row += f"{score:>6.1f}"
            print(row)
        
        print("----------")