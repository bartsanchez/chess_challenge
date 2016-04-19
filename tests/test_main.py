from chess_challenge import main


def test_solve():
    assert main.solve(1, 1, 'foo') == 0
