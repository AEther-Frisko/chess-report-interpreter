"""Main entry point for the chess report interpreter application."""

from chess_report_interpreter.file.tms import read_tms_file
from chess_report_interpreter.tournament.player import ChessPlayer
from chess_report_interpreter.tournament.result import ChessTournamentResult
from chess_report_interpreter.tournament.tournament import ChessTournament

# TOURNEY_FILE = "20250621-KWCC June Active Swiss.tms"
TOURNEY_FILE = "data.tms.sample"

def main():
    players = read_tms_file(TOURNEY_FILE)
    tournament = ChessTournament("June Active Swiss", "KWCC", "2025-06-21")
    for player_data in players:
        seed_no = int(player_data[0])
        name = player_data[1]
        cfc_id = int(player_data[2])
        cfc_rating = int(player_data[3])
        results = [ChessTournamentResult(result) for result in player_data[4:] if result]
        chess_player = ChessPlayer(seed_no, name, cfc_id, cfc_rating, results)
        tournament.add_player(chess_player)

    print(tournament.get_tournament_details())
    print("Players sorted by seed:")
    for player in tournament.get_players_by_seed():
        print(player.get_player_details(), "Results: " + player.get_player_results())
    #print("Players sorted by rating:")
    #for player in tournament.get_players_by_rating():
    #    print(player)


if __name__ == "__main__":
    main()
