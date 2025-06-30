#   Author:     Max Venables
#   Purpose:    Reads and interprets .tms files, storing the data in a Player class

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