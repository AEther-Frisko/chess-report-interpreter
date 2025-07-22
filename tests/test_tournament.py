from chess_report_interpreter.tournament.player import ChessPlayer
from chess_report_interpreter.tournament.result import ChessResult, ResultEnum
from chess_report_interpreter.tournament.tournament import ChessTournament


def test_valid_initialization():
    p1 = ChessPlayer(1, "Guy, One", 100000, 1990, [ChessResult("W2"), ChessResult("W3")])
    p2 = ChessPlayer(2, "Guy, Number Two", 100001, 1980, [ChessResult("L1"), ChessResult("W3")])
    p3 = ChessPlayer(3, "Last, Guy", 100002, 1970, [ChessResult("L2"), ChessResult("L1")])
    players = {
        1 : p1,
        2 : p2,
        3 : p3
    }
    tournament = ChessTournament(players)

    assert tournament.players == players

def test_get_valid_seed():
    p1 = ChessPlayer(1, "Guy, One", 100000, 1990, [ChessResult("W2"), ChessResult("W3")])
    p2 = ChessPlayer(2, "Guy, Number Two", 100001, 1980, [ChessResult("L1"), ChessResult("W3")])
    p3 = ChessPlayer(3, "Last, Guy", 100002, 1970, [ChessResult("L2"), ChessResult("L1")])
    players = {
        1 : p1,
        2 : p2,
        3 : p3
    }
    tournament = ChessTournament(players)
    retrieved = tournament.get_player(2)

    assert retrieved == p2

def test_get_invalid_seed():
    p1 = ChessPlayer(1, "Guy, One", 100000, 1990, [ChessResult("W2"), ChessResult("W3")])
    p2 = ChessPlayer(2, "Guy, Number Two", 100001, 1980, [ChessResult("L1"), ChessResult("W3")])
    p3 = ChessPlayer(3, "Last, Guy", 100002, 1970, [ChessResult("L2"), ChessResult("L1")])
    players = {
        1 : p1,
        2 : p2,
        3 : p3
    }
    tournament = ChessTournament(players)
    retrieved = tournament.get_player(10)

    assert retrieved is None

def test_get_proper_name():
    p1 = ChessPlayer(1, "Guy, One", 100000, 1990, [ChessResult("W2"), ChessResult("W3")])
    p2 = ChessPlayer(2, "Guy, Number Two", 100001, 1980, [ChessResult("L1"), ChessResult("W3")])
    p3 = ChessPlayer(3, "Last, Guy", 100002, 1970, [ChessResult("L2"), ChessResult("L1")])
    players = {
        1 : p1,
        2 : p2,
        3 : p3
    }
    tournament = ChessTournament(players)
    retrieved = tournament.get_player_by_name("Last, Guy")

    assert retrieved == p3

def test_get_lowercase_name():
    p1 = ChessPlayer(1, "Guy, One", 100000, 1990, [ChessResult("W2"), ChessResult("W3")])
    p2 = ChessPlayer(2, "Guy, Number Two", 100001, 1980, [ChessResult("L1"), ChessResult("W3")])
    p3 = ChessPlayer(3, "Last, Guy", 100002, 1970, [ChessResult("L2"), ChessResult("L1")])
    players = {
        1 : p1,
        2 : p2,
        3 : p3
    }
    tournament = ChessTournament(players)
    retrieved = tournament.get_player_by_name("guy, one")

    assert retrieved == p1

def test_get_invalid_name():
    p1 = ChessPlayer(1, "Guy, One", 100000, 1990, [ChessResult("W2"), ChessResult("W3")])
    p2 = ChessPlayer(2, "Guy, Number Two", 100001, 1980, [ChessResult("L1"), ChessResult("W3")])
    p3 = ChessPlayer(3, "Last, Guy", 100002, 1970, [ChessResult("L2"), ChessResult("L1")])
    players = {
        1 : p1,
        2 : p2,
        3 : p3
    }
    tournament = ChessTournament(players)
    retrieved = tournament.get_player_by_name("not on this list")

    assert retrieved is None

def test_create_valid_report():
    p1 = ChessPlayer(1, "Guy, One", 100000, 1990, [ChessResult("W2"), ChessResult("W3")])
    p2 = ChessPlayer(2, "Guy, Number Two", 100001, 1980, [ChessResult("L1"), ChessResult("W3")])
    p3 = ChessPlayer(3, "Last, Guy", 100002, 1970, [ChessResult("L2"), ChessResult("L1")])
    players = {
        1 : p1,
        2 : p2,
        3 : p3
    }
    tournament = ChessTournament(players)
    report = tournament.create_report(1)

    assert report[0][0].value is ResultEnum.WIN.value
    assert report[0][1] == "Guy, Number Two"
    assert report[1][0].value is ResultEnum.WIN.value
    assert report[1][1] == "Last, Guy"

def test_no_opponent_name():
    p1 = ChessPlayer(1, "Guy, One", 100000, 1990, [ChessResult("W2"), ChessResult("L0")])
    p2 = ChessPlayer(2, "Guy, Number Two", 100001, 1980, [ChessResult("L1"), ChessResult("W3")])
    p3 = ChessPlayer(3, "Last, Guy", 100002, 1970, [ChessResult("L2"), ChessResult("L0")])
    players = {
        1 : p1,
        2 : p2,
        3 : p3
    }
    tournament = ChessTournament(players)
    report = tournament.create_report(1)

    assert report[1][0].value is ResultEnum.LOSS.value
    assert report[1][1] == "NA"