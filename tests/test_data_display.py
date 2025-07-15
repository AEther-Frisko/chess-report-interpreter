from chess_report_interpreter.tournament.data_display import DataDisplay
from chess_report_interpreter.tournament.player import ChessPlayer
from chess_report_interpreter.tournament.result import ChessResult, ResultEnum
from chess_report_interpreter.tournament.tournament import ChessTournament


def test_player_brief_display(capsys):
    player = ChessPlayer(1, "Player", 123456, 1977, [])
    
    DataDisplay.display_player_brief(player)
    output = capsys.readouterr().out

    assert "Name:         Player" in output
    assert "CFC ID:       123456" in output
    assert "CFC Rating:   1977" in output

def test_player_report_display(capsys):
    results = [
        (ResultEnum.WIN, "Guy 1"),
        (ResultEnum.DRAW, "Another Guy"),
        (ResultEnum.LOSS, "Some Other Guy")
    ]
    
    DataDisplay.display_player_report(results)
    output = capsys.readouterr().out

    assert "Round:    1" in output
    assert "Opponent: Guy 1" in output
    assert "Result:   Win" in output
    assert "Round:    2" in output
    assert "Opponent: Another Guy" in output
    assert "Result:   Draw" in output
    assert "Round:    3" in output
    assert "Opponent: Some Other Guy" in output
    assert "Result:   Loss" in output

def test_leaderboard_display(capsys):
    p1 = ChessPlayer(1, "Guy 1", 12345, 2000, [])
    p2 = ChessPlayer(2, "Guy 2", 23456, 1900, [])
    tournament = ChessTournament({1: p1, 2: p2})
    top_players = [(1, 2.5), (2, 2.0)]

    DataDisplay.display_leaderboard(top_players, tournament)
    output = capsys.readouterr().out
    
    assert "1." in output
    assert "Guy 1" in output
    assert "2.5" in output
    assert "2." in output
    assert "Guy 2" in output
    assert "2.0" in output

def test_round_overview_display(capsys):
    p1 = ChessPlayer(1, "Person One", 100001, 2000, [ChessResult("W2"), ChessResult("D3")])
    p2 = ChessPlayer(2, "Person Two", 100002, 1900, [ChessResult("L1"), ChessResult("W3")])
    p3 = ChessPlayer(3, "Person Three", 100003, 1800, [ChessResult("D1"), ChessResult("L2")])
    
    players = {1: p1, 2: p2, 3: p3}
    tournament = ChessTournament(players)

    DataDisplay.display_round_overview(tournament)
    output = capsys.readouterr().out

    assert "Player" in output
    assert "R1" in output and "R2" in output
    assert "Total" in output

    assert "W2" in output
    assert "D3" in output
    assert "L1" in output
    assert "Person One" in output
    assert "Person Two" in output
    assert "Person Three" in output

    assert "1.5" in output
    assert "1.0" in output
    assert "0.5" in output

def test_round_overview_blank_result(capsys):
    p1 = ChessPlayer(1, "Person One", 100001, 2000, [ChessResult("bad data"), ChessResult("bad data")])
    p2 = ChessPlayer(2, "Person Two", 100002, 1900, [ChessResult("L1"), ChessResult("W3")])
    p3 = ChessPlayer(3, "Person Three", 100003, 1800, [ChessResult("D1"), ChessResult("L2")])
    
    players = {1: p1, 2: p2, 3: p3}
    tournament = ChessTournament(players)

    DataDisplay.display_round_overview(tournament)
    output = capsys.readouterr().out

    assert "NA" in output