"""Main entry point for the chess report interpreter application."""

from src.chess_report_interpreter.tournament.player import ChessPlayer
from src.chess_report_interpreter.tournament.result import ChessTournamentResult


if __name__ == "__main__":
    # Example usage
    results = [ChessTournamentResult("W3"), ChessTournamentResult("L2"), ChessTournamentResult("D4")]
    player = ChessPlayer(1, "John Doe", 12345, 2000, results)
    print(player)
