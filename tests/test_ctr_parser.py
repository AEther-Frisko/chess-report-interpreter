from chess_report_interpreter.tournament.ctr_parser import ctrParser
from chess_report_interpreter.tournament.tournament import ChessTournament


def test_parse_data_valid():
    line = ctrParser.read_file("data/swiss_data.ctr.sample")[0]
    data = ctrParser.parse_tournament_data(line)
    tournament = ChessTournament({}, data)

    assert tournament.event == "Example Tournament"
    assert tournament.province == "ON"
    assert tournament.ref_num == ""
    assert tournament.pairing == "S"
    assert tournament.end_date == "2025/07/21"
    assert tournament.player_total == "4"
    assert tournament.round_total == "3"
    assert tournament.type == "A"
    assert tournament.org_id == "111111"
    assert tournament.arb_id == "111111"

def test_parse_data_invalid():
    data = ctrParser.parse_tournament_data("This is bad data, lol.")

    assert data is None