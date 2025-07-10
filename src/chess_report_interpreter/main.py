"""Main entry point for the chess report interpreter application."""

import sys
import argparse
from tournament.tms_parser import tmsParser
from tournament.tournament import ChessTournament
from tournament.data_display import DataDisplay
from tournament.data_analyzer import TournamentAnalyzer


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--tms", help="The name of the tms file to read", required=True)
    args = parser.parse_args()
    filename = args.tms

    # Example usage
    lines = tmsParser.read_file(filename)
    players: dict = tmsParser.parse_lines(lines)
    tournament = ChessTournament(players)

    while True:
        print(
            "Would you like to: "
            "\n1) See all players"
            "\n2) See a specific player's report"
            "\n3) See the top three players by score"
            "\n4) See an overview of all games in the tournament"
            "\n5) Quit")
        
        match input():
            case "1":
                print("--- PLAYER LIST ---")
                for player in tournament.players:
                    DataDisplay.display_player_brief(tournament.get_player(player))
            
            case "2":
                print("Please input the player's name (last, first): ")
                name = input()
                result = tournament.get_player_by_name(name)
                if result != None:
                    DataDisplay.display_player_brief(result)
                    report = tournament.create_report(result.seed)
                    DataDisplay.display_player_report(report)
                else:
                    print("This player could not be found.")
            
            case "3":
                top_three = TournamentAnalyzer.get_top_three(tournament)
                DataDisplay.display_leaderboard(top_three, tournament)

            case "4":
                DataDisplay.display_round_overview(tournament)

            case "5":
                print("Exiting program...")
                sys.exit()

            case _:
                print("Invalid input, please try again.")


if __name__ == "__main__":
    main()
