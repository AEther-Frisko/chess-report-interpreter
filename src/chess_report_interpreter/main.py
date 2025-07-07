"""Main entry point for the chess report interpreter application."""

import sys
from tournament.tms_parser import tmsParser
from tournament.tournament import ChessTournament


if __name__ == "__main__":
    # Example usage
    lines = tmsParser.read_file("data.tms.sample")
    players: dict = tmsParser.parse_lines(lines)
    tournament = ChessTournament(players)
    
    while(True):
        print("Would you like to: " \
            "\n1) See all player data"
            "\n2) See a specific player's report"
            "\n3) quit")
        
        match int(input()):
            case 1:
                for player in tournament.players:
                    print(tournament.get_player(player))
            
            case 2:
                print("Please input the player's name (last, first): ")
                name = input()
                result = tournament.get_player_by_name(name)
                if result != None:
                    tournament.display_report(result.seed)
                else:
                    print("This user could not be found.")
            
            case 3:
                print("Exiting program...")
                sys.exit()
            
            case _:
                print("Invalid input, please try again.")