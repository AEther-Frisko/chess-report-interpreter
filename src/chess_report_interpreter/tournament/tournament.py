"""Module for compiling all player data for a tournament."""

from .result import ResultEnum
from .player import ChessPlayer


class ChessTournament:
    """A class representing all the results of a chess tournament."""

    def __init__(self, players: dict[int, ChessPlayer], data: list[str] | None):
        """Initializes a tournament instance."""
        self.players = players
        
        if data is not None:
            self.event = data[0]
            self.province = data[1]
            self.ref_num = data[2]
            self.pairing = data[3]
            self.end_date = data[4]
            self.player_total = int(data[5])
            self.round_total = int(data[6])
            self.type = data[7]
            self.org_id = int(data[8])
            self.arb_id = int(data[9])

    def get_player(self, seed: int):
        """Returns a Player via the seed value."""
        return self.players.get(seed)

    def get_player_by_name(self, name: str):
        """Returns a Player via the name value."""
        for player in self.players.values():
            if player.name.lower() == name.lower():
                return player
        return None
    
    def create_report(self, seed: int):
        """Creates a report of a player's tournament results."""
        results: list[tuple[ResultEnum, str]] = []
        player = self.get_player(seed)
        for result in player.results:
            outcome = ResultEnum.from_code(result.result)
            opponent = self.get_player(result.vs_seed)
            if opponent is not None:
                results.append((outcome, opponent.name))
            else:
                results.append((outcome, "NA"))
        return results
