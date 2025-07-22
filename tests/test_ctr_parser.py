from chess_report_interpreter.tournament.ctr_parser import ctrParser
from chess_report_interpreter.tournament.tournament import ChessTournament


def test_parse_data_valid():
    line = ctrParser.read_file("data/swiss_data.ctr.sample")[0]
    data = ctrParser.parse_tournament_data(line)
    tournament = ChessTournament({}, data)

    assert tournament.info["Event"] == "Example Tournament"
    assert tournament.info["Province"] == "ON"
    assert tournament.info["Reference Number"] == ""
    assert tournament.info["Pairings"] == "Swiss"
    assert tournament.info["End Date"] == "2025/07/21"
    assert tournament.info["Player Total"] == 4
    assert tournament.info["Round Total"] == 3
    assert tournament.info["Format"] == "Active"
    assert tournament.info["Organizer"] == 111111
    assert tournament.info["Arbiter"] == 111111

def test_parse_data_invalid():
    data = ctrParser.parse_tournament_data("This is bad data, lol.")

    assert data is None