"""File reader for TMS (Tournament Management System) files."""


def read_tms_file(filename: str) -> list[list[str]]:
    """Reads a TMS file and returns a list of tournament data."""
    players = []
    try:
        with open(filename, "r", encoding="utf8") as file:
            for line in file:
                player_data = line.strip().split("\t")
                players.append(player_data)
    except FileNotFoundError:
        print(f"ERROR: The file '{filename}' does not exist or cannot be found.")
    return players
