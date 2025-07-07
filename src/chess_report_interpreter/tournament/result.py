"""Result module for chess tournament results."""

from enum import Enum


class ResultEnum(Enum):
    """An enumeration representing the possible results of a chess game."""

    WIN = "Win"
    LOSS = "Loss"
    DRAW = "Draw"

    @classmethod
    def from_code(cls, code: str):
        """Converts a single character code to a ResultEnum."""
        mapping = {"W": cls.WIN, "L": cls.LOSS, "D": cls.DRAW}
        return mapping.get(code)

    def __str__(self):
        return self.value


class ChessResult:
    """A class representing the result of a chess tournament for a player."""

    def __init__(self, result: str):
        """Initializes a ChessResult instance."""
        # Extract the result code as the first character.
        # The rest of the string should be the opponent's seed number.
        # Example: "W1" means a win against seed 1.
        if result and result[0] in {"W", "L", "D"}:
            self.result: str = result[0]
            number_part = result[1:]
            self.vs_seed: int = (
                int("".join(filter(str.isdigit, number_part))) if number_part else None
            )
        else:
            self.result = None
            self.vs_seed = None

    def __str__(self):
        """Returns a string representation of the ChessResult."""
        return f"Vs Seed: {self.vs_seed}, Result: {ResultEnum.from_code(self.result)}"
