from chess_challenge import main


class TestSolve:
    def test_solve(self):
        result = {
            ('K', 'K', 'R'): [set([(0, 0), (2, 0), (1, 2)])],
            ('K', 'R', 'K'): [
                set([(0, 0), (2, 1), (0, 2)]),
                set([(2, 0), (0, 1), (2, 2)]),
            ],
            ('R', 'K', 'K'): [set([(1, 0), (0, 2), (2, 2)])],
        }
        assert main.solve(3, 3, ['K', 'K', 'R']) == result


class TestSolvePieces:
    def test_solve__valid_pieces(self):
        result = {('K',): [set([(0, 0)])]}
        assert main.solve(1, 1, ['K']) == result

    def test_solve__invalid_pieces(self):
        assert main.solve(1, 1, [0]) == -1
