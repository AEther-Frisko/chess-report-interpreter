from chess_report_interpreter.tournament.tms_parser import tmsParser


def test_read_valid_file():
    lines = tmsParser.read_file("data/data.tms.sample")
    
    assert lines[0] == "1\tDeleon, Zach\t100000\t1970\tD2\tW3\tW4\t\n"
    assert lines[1] == "2\tWalsh, Bruce\t100001\t1935\tD1\tW4\tW3\t\n"
    assert lines[2] == "3\tCrane, Vincent\t100002\t1930\tW4\tL1\tL2\t\n"
    assert lines[3] == "4\tVan Damme, Frances\t100003\t1890\tL3\tL2\tL1\t"

def test_read_invalid_file():
    lines = tmsParser.read_file("not a file")

    assert lines == None

def test_parse_lines():
    lines = tmsParser.read_file("data/data.tms.sample")
    players = tmsParser.parse_lines(lines)
    p1 = players.get(1)

    assert p1.seed == 1
    assert p1.name == "Deleon, Zach"
    assert p1.cfc_id == 100000
    assert p1.cfc_rating == 1970
    assert p1.results[0].result == "D" and p1.results[0].vs_seed == 2
    assert p1.results[1].result == "W" and p1.results[1].vs_seed == 3
    assert p1.results[2].result == "W" and p1.results[2].vs_seed == 4