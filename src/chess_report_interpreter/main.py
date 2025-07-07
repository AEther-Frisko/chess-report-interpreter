"""Main entry point for the chess report interpreter application."""

from tournament.tms_parser import tmsParser
from tournament.tournament import ChessTournament


if __name__ == "__main__":
    # Example usage
    lines = tmsParser.read_file("data.tms.sample")
    players: dict = tmsParser.parse_lines(lines)
    tournament = ChessTournament(players)
    
    for player in tournament.players:
        print(tournament.get_player(player))