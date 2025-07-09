from chess_report_interpreter.tournament.result import ChessResult
from src.chess_report_interpreter.tournament.player import ChessPlayer


def test_valid_initialization():
    results = [ChessResult("W4"), ChessResult("D3"), ChessResult("L2")]
    player = ChessPlayer(1, "Some, Guy", 111111, 1987, results)

    assert player.seed == 1
    assert player.name == "Some, Guy"
    assert player.cfc_id == 111111
    assert player.cfc_rating == 1987
    assert player.results == results

def test_str_output():
    results = [ChessResult("W3"), ChessResult("L1")]
    player = ChessPlayer(2, "Smith, John", 123456, 1972, results)
    output = str(player)

    assert "Seed:       2" in output
    assert "Name:       Smith, John" in output
    assert "CFC ID:     123456" in output
    assert "CFC Rating: 1972" in output
    assert "Vs Seed: 3, Result: Win" in output
    assert "Vs Seed: 1, Result: Loss" in output