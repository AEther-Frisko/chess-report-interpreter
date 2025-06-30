#   Author:     Max Venables
#   Purpose:    Reads and interprets .tms files, displaying the results

import sys


class Player:
    def __init__(self, seed, name, cfcID, cfcRating, results):
        self.seed = seed
        self.name = name
        self.cfcID = cfcID
        self.cfcRating = cfcRating
        self.results = results
    
    def __str__(self):
        return f"Seed:       {self.seed}\
                \nName:       {self.name}\
                \nCFC ID:     {self.cfcID}\
                \nCFC Rating: {self.cfcRating}\
                \nResults:    {self.results} \n"


#   Takes in a filename, and populates a dict with
#   parsed versions of each line of the file.
#   Returns the dict of parsed data.
def readFile(filename: str):
    players = {}
    try:
        file = open(filename)
        for line in file:
            p = parseLine(line)
            players[p.name] = p
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

    p = Player(seed, name, cfcID, cfcRating, results)
    return p


def displayReport(p: Player, players: dict):
    print("  Round  |  Result  |  Opponent  |")
    for result in p.results:
        round = p.results.index(result) + 1
        res = "?"
        opp = "?"
        
        # determine result
        if "W" in result:
            res = "Win"
        elif "L" in result:
            res = "Loss"
        elif "D" in result:
            res = "Draw"
        else:
            print("This shouldn't be possible.")
        
        # determine opponent
        seed = result[1:]
        for player in players.values():
            if player.seed == seed:
                opp = player.name

        # display round data
        print(f"  {round:<9}|  {res:<10}|  {opp:<12}")


#   --- Main program ---
filename = "data.tms"   # TODO: switch this out for arg parsing
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
            key = input()
            if key in players.keys():
                print(players[key])
                displayReport(players[key], players)
            else:
                print("This seed does not exist.")
        case 3:
            print("Exiting program...")
            sys.exit()
        case _:
            print("Not a valid input.")