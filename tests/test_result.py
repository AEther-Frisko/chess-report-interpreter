from chess_report_interpreter.tournament.result import ChessResult, ResultEnum


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
    assert result.result is None and result.vs_seed is None

def test_invalid_seed():
    result = ChessResult("WEEE")
    assert result.result == "W" and result.vs_seed is None

def test_missing_seed():
    result = ChessResult("L")
    assert result.result == "L" and result.vs_seed is None

def test_missing_result():
    result = ChessResult("5")
    assert result.result is None and result.vs_seed is None

def test_completely_invalid():
    result = ChessResult("This is not the right format!1!!")
    assert result.result is None and result.vs_seed is None

def test_str_output_win():
    result = ChessResult("W6")
    output = str(result)
    assert "Vs Seed: 6, Result: Win" in output

def test_str_output_loss():
    result = ChessResult("L7")
    output = str(result)
    assert "Vs Seed: 7, Result: Loss" in output

def test_str_output_draw():
    result = ChessResult("D7")
    output = str(result)
    assert "Vs Seed: 7, Result: Draw" in output

def test_valid_win_enum():
    result = ResultEnum.from_code("W")
    assert result is ResultEnum.WIN

def test_valid_loss_enum():
    result = ResultEnum.from_code("L")
    assert result is ResultEnum.LOSS

def test_valid_draw_enum():
    result = ResultEnum.from_code("D")
    assert result is ResultEnum.DRAW

def test_invalid_enum():
    result = ResultEnum.from_code("A")
    assert result is None