from chess_report_interpreter.tournament.tms_parser import tmsParser


def test_read_valid_file():
    lines = tmsParser.read_file("data/swiss_data.tms.sample")
    
    assert lines[0] == "1\tDeleon, Zach\t100000\t1970\tD2\tW3\tW4\t\n"
    assert lines[1] == "2\tWalsh, Bruce\t100001\t1935\tD1\tW4\tW3\t\n"
    assert lines[2] == "3\tCrane, Vincent\t100002\t1930\tW4\tL1\tL2\t\n"
    assert lines[3] == "4\tVan Damme, Frances\t100003\t1890\tL3\tL2\tL1\t"

def test_read_invalid_file():
    lines = tmsParser.read_file("not a file")

    assert lines is None

def test_parse_lines():
    lines = tmsParser.read_file("data/swiss_data.tms.sample")
    players = tmsParser.parse_lines(lines)
    p = players.get(1)

    assert p.seed == 1
    assert p.name == "Deleon, Zach"
    assert p.cfc_id == 100000
    assert p.cfc_rating == 1970
    assert p.results[0].result == "D" and p.results[0].vs_seed == 2
    assert p.results[1].result == "W" and p.results[1].vs_seed == 3
    assert p.results[2].result == "W" and p.results[2].vs_seed == 4

def test_parse_round_robin():
    lines = tmsParser.read_file("data/rr_data.tms.sample")
    players = tmsParser.parse_lines(lines)
    p = players.get(2)

    assert p.seed == 2
    assert p.name == "Walsh, Bruce"
    assert p.cfc_id == 100001
    assert p.cfc_rating == 1935
    assert p.results[0].result == "D" and p.results[0].vs_seed == 1
    assert p.results[1].result == "W" and p.results[1].vs_seed == 3
    assert p.results[2].result == "W" and p.results[2].vs_seed == 4