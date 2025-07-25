from chess_report_interpreter.tournament.data_analyzer import PointValueEnum
from chess_report_interpreter.tournament.data_analyzer import TournamentAnalyzer
from chess_report_interpreter.tournament.player import ChessPlayer
from chess_report_interpreter.tournament.result import ChessResult
from chess_report_interpreter.tournament.tournament import ChessTournament


def test_valid_enum_win():
    result = PointValueEnum.from_result("W")
    assert result == PointValueEnum.WIN.value

def test_valid_enum_loss():
    result = PointValueEnum.from_result("L")
    assert result == PointValueEnum.LOSS.value

def test_valid_enum_draw():
    result = PointValueEnum.from_result("D")
    assert result == PointValueEnum.DRAW.value

def test_invalid_enum():
    result = PointValueEnum.from_result("Z")
    assert result == 0.0

def test_valid_top_three():
    players = {
        1 : ChessPlayer(1, "Top, Player", 123456, 1990, [ChessResult("W2"), ChessResult("W3"), ChessResult("W4")]),
        2 : ChessPlayer(2, "Number, Two", 122222, 1985, [ChessResult("L1"), ChessResult("W4"), ChessResult("W3")]),
        3 : ChessPlayer(3, "Third, Guy", 100003, 1980, [ChessResult("W4"), ChessResult("L1"), ChessResult("L2")]),
        4 : ChessPlayer(4, "Loser, Dude", 100000, 1970, [ChessResult("L3"), ChessResult("L2"), ChessResult("L1")])
    }
    tournament = ChessTournament(players, None)
    top_three = TournamentAnalyzer.get_top_three(tournament)

    assert top_three[0][0] == 1
    assert top_three[0][1] == 3.0
    assert top_three[1][0] == 2
    assert top_three[1][1] == 2.0
    assert top_three[2][0] == 3
    assert top_three[2][1] == 1.0

def test_top_three_two_players():
    players = {
        1 : ChessPlayer(1, "Winner, Guy", 111111, 1999, [ChessResult("W2")]),
        2 : ChessPlayer(2, "Loser, Dude", 100000, 1970, [ChessResult("L1")])
    }
    tournament = ChessTournament(players, None)
    top_three = TournamentAnalyzer.get_top_three(tournament)

    assert top_three[0][0] == 1
    assert top_three[0][1] == 1.0
    assert top_three[1][0] == 2
    assert top_three[1][1] == 0.0

def test_top_three_tie():
    players = {
        1 : ChessPlayer(1, "Top, Player", 123456, 1990, [ChessResult("W2"), ChessResult("W3"), ChessResult("W4")]),
        2 : ChessPlayer(2, "Number, Two", 122222, 1985, [ChessResult("L1"), ChessResult("W4"), ChessResult("D3")]),
        3 : ChessPlayer(3, "Third, Guy", 100003, 1980, [ChessResult("W4"), ChessResult("L1"), ChessResult("D2")]),
        4 : ChessPlayer(4, "Loser, Dude", 100000, 1970, [ChessResult("L3"), ChessResult("L2"), ChessResult("L1")])
    }
    tournament = ChessTournament(players, None)
    top_three = TournamentAnalyzer.get_top_three(tournament)

    assert top_three[0][0] == 1
    assert top_three[0][1] == 3.0
    assert top_three[1][0] == 2
    assert top_three[1][1] == 1.5
    assert top_three[2][0] == 3
    assert top_three[2][1] == 1.5

def test_highest_under_rating():
    players = {
        1 : ChessPlayer(1, "Top, Player", 123456, 1990, [ChessResult("W2"), ChessResult("W3"), ChessResult("W4")]),
        2 : ChessPlayer(2, "Number, Two", 122222, 1985, [ChessResult("L1"), ChessResult("W4"), ChessResult("D3")]),
        3 : ChessPlayer(3, "Third, Guy", 100003, 1980, [ChessResult("W4"), ChessResult("L1"), ChessResult("D2")]),
        4 : ChessPlayer(4, "Loser, Dude", 100000, 1970, [ChessResult("L3"), ChessResult("L2"), ChessResult("L1")])
    }
    tournament = ChessTournament(players, None)
    highest = TournamentAnalyzer.get_top_under_rating(tournament, 1982)

    assert highest["Score"] == 1.5
    assert highest["Player"].name == "Third, Guy"
    assert highest["Max Rating"] == 1982