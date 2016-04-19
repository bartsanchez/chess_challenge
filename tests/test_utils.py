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


class TestNextPosition:
    def test_get_next_position__left_top_corner(self):
        assert utils.get_next_position(0, 0, 3, 3) == (1, 0)

    def test_get_next_position__center(self):
        assert utils.get_next_position(1, 1, 3, 3,) == (2, 1)

    def test_get_next_position__change_row(self):
        assert utils.get_next_position(2, 0, 3, 3) == (0, 1)

    def test_get_next_position__last_position(self):
        assert utils.get_next_position(2, 2, 3, 3) == (False, False)
