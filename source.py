#   Author:     Max Venables
#   Purpose:    Reads and interprets .tms files, displaying the results

import sys
import tms_fileio


#   --- Main program ---
print("Please enter the data file you wish to parse: ")
filename = input()   # TODO: switch this out for arg parsing
players = tms_fileio.readFile(filename)

while(True):
    print("Would you like to: " \
        "\n1) See all player data"
        "\n2) See a specific player's report"
        "\n3) quit")

    match int(input()):
        case 1:
            for key in players:
                print(players[key])
        case 2:
            print("Please input the player's name (last, first): ")
            key = input().lower()
            if key in players.keys():
                print(players[key])
                players[key].displayReport(players)
            else:
                print("This seed does not exist.")
        case 3:
            print("Exiting program...")
            sys.exit()
        case _:
            print("Not a valid input.")