from chess_report_interpreter.tournament.data_display import DataDisplay
from chess_report_interpreter.tournament.player import ChessPlayer
from chess_report_interpreter.tournament.result import ResultEnum
from chess_report_interpreter.tournament.tournament import ChessTournament


def test_player_brief_display(capsys):
    player = ChessPlayer(1, "Player", 123456, 1977, [])
    
    DataDisplay.display_player_brief(player)
    output = capsys.readouterr()

    assert "Name:         Player" in output.out
    assert "CFC ID:       123456" in output.out
    assert "CFC Rating:   1977" in output.out

def test_player_report_display(capsys):
    results = [
        (ResultEnum.WIN, "Guy 1"),
        (ResultEnum.DRAW, "Another Guy"),
        (ResultEnum.LOSS, "Some Other Guy")
    ]
    
    DataDisplay.display_player_report(results)
    output = capsys.readouterr()

    assert "--- PLAYER TOURNAMENT RESULTS ---" in output.out
    assert "Round:    1" in output.out
    assert "Opponent: Guy 1" in output.out
    assert "Result:   Win" in output.out
    assert "Round:    2" in output.out
    assert "Opponent: Another Guy" in output.out
    assert "Result:   Draw" in output.out
    assert "Round:    3" in output.out
    assert "Opponent: Some Other Guy" in output.out
    assert "Result:   Loss" in output.out

def test_leaderboard_display(capsys):
    p1 = ChessPlayer(1, "Guy 1", 12345, 2000, [])
    p2 = ChessPlayer(2, "Guy 2", 23456, 1900, [])
    tournament = ChessTournament({1: p1, 2: p2})
    top_players = [(1, 2.5), (2, 2.0)]

    DataDisplay.display_leaderboard(top_players, tournament)
    captured = capsys.readouterr()
    
    assert "--- TOP PLAYERS ---" in captured.out
    assert "1." in captured.out
    assert "Guy 1" in captured.out
    assert "2.5" in captured.out
    assert "2." in captured.out
    assert "Guy 2" in captured.out
    assert "2.0" in captured.out