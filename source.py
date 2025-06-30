#   Author:     Max Venables
#   Purpose:    Reads and interprets .tms files, displaying the results

import sys
import player

#   Takes in a filename, and populates a dict with
#   parsed versions of each line of the file.
#   Returns the dict of parsed data.
def readFile(filename: str):
    players = {}
    try:
        file = open(filename)
        for line in file:
            p = parseLine(line)
            players[p.name.lower()] = p
        file.close()
    except:
        print("ERROR: This file does not exist or cannot be found.")
    return players


#   Takes in a string, and splits it according to
#   the formatting of a .tms file.
#   Returns a Player class with the parsed data.
def parseLine(line: str):
    data = line.split("	")
    
    seed = data[0]
    name = data[1]
    cfcID = data[2]
    cfcRating = data[3]
    results = data[4:]
    del results[-1]

    p = player.Player(seed, name, cfcID, cfcRating, results)
    return p


#   --- Main program ---
print("Please enter the data file you wish to parse: ")
filename = input()   # TODO: switch this out for arg parsing
players = readFile(filename)

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