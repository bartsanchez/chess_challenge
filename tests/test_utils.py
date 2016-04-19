from chess_challenge import utils


class TestPieces:
    def test_are_valid_pieces__yes(self):
        assert utils.are_valid_pieces(['K', 'K', 'K', 'R']) is True

    def test_are_valid_pieces__false(self):
        assert utils.are_valid_pieces(['K', 'A', 'R']) is False


class TestPiecesCombinations:
    def test_pieces_combinations__K(self):
        assert utils.get_pieces_combinations(['K']) == set([('K',)])

    def test_pieces_combinations__KK(self):
        result = set([('K', 'K')])
        assert utils.get_pieces_combinations(['K', 'K']) == result

    def test_pieces_combinations__KKR(self):
        result = set([('K', 'K', 'R'), ('K', 'R', 'K'), ('R', 'K', 'K')])
        assert utils.get_pieces_combinations(['K', 'K', 'R']) == result
