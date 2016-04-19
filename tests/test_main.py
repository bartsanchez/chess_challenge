from chess_challenge import main


class TestSolve:
    def test_solve(self):
        assert main.solve(1, 1, ['K']) == 0


class TestSolvePieces:
    def test_solve__valid_pieces(self):
        assert main.solve(1, 1, ['K']) == 0

    def test_solve__invalid_pieces(self):
        assert main.solve(1, 1, [0]) == -1
