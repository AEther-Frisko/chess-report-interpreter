#   Author:     Max Venables
#   Purpose:    The Player class for the tms file interpreter.
#               Stores data read in from a .tms file, and displays it.


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
    
    #   Takes in a dict of all players.
    #   Prints a table of round results for the player, in a
    #   more readable format (ie. converting seed numbers to
    #   player names).
    def displayReport(self, players: dict):
        print("  Round  |  Result  |  Opponent  |")
        for result in self.results:
            round = self.results.index(result) + 1
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