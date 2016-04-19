from chess_challenge import utils


class TestPieces:
    def test_are_valid_pieces__yes(self):
        assert utils.are_valid_pieces(['K', 'K', 'K', 'R']) is True

    def test_are_valid_pieces__false(self):
        assert utils.are_valid_pieces(['K', 'A', 'R']) is False
