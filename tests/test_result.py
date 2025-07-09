from src.chess_report_interpreter.tournament.result import ChessResult
from src.chess_report_interpreter.tournament.result import ResultEnum

def test_proper_win():
    result = ChessResult("W1")
    assert result.result == "W" and result.vs_seed == 1

def test_proper_loss():
    result = ChessResult("L2")
    assert result.result == "L" and result.vs_seed == 2

def test_proper_draw():
    result = ChessResult("D3")
    assert result.result == "D" and result.vs_seed == 3

def test_invalid_result():
    result = ChessResult("A4")
    assert result.result == None and result.vs_seed == None

def test_invalid_seed():
    result = ChessResult("WEEE")
    assert result.result == "W" and result.vs_seed == None

def test_missing_seed():
    result = ChessResult("L")
    assert result.result == "L" and result.vs_seed == None

def test_missing_result():
    result = ChessResult("5")
    assert result.result == None and result.vs_seed == None

def test_completely_invalid():
    result = ChessResult("This is not the right format!1!!")
    assert result.result == None and result.vs_seed == None

def test_valid_win_enum():
    result = ResultEnum.from_code("W")
    assert result == ResultEnum.WIN

def test_valid_loss_enum():
    result = ResultEnum.from_code("L")
    assert result == ResultEnum.LOSS

def test_valid_draw_enum():
    result = ResultEnum.from_code("D")
    assert result == ResultEnum.DRAW

def test_invalid_enum():
    result = ResultEnum.from_code("A")
    assert result == None