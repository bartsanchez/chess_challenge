import mock

from chess_challenge import pieces


class TestMenacedPositionsCalls:
    @mock.patch('chess_challenge.pieces.get_menaced_king_positions')
    def test_calling_king(self, king_mock):
        pieces.get_menaced_positions('K', (0, 0), 3, 3)
        king_mock.assert_called_once_with((0, 0), 3, 3)

    @mock.patch('chess_challenge.pieces.get_menaced_rook_positions')
    def test_calling_rook(self, rook_mock):
        pieces.get_menaced_positions('R', (0, 0), 3, 3)
        rook_mock.assert_called_once_with((0, 0), 3, 3)

    @mock.patch('chess_challenge.pieces.get_menaced_bishop_positions')
    def test_calling_bishop(self, bishop_mock):
        pieces.get_menaced_positions('B', (0, 0), 3, 3)
        bishop_mock.assert_called_once_with((0, 0), 3, 3)


class TestKing:
    def test_menaced_king_positions__left_top_corner(self):
        result = [(1, 0), (0, 1), (1, 1)]
        assert pieces.get_menaced_king_positions((0, 0), 3, 3) == result

    def test_menaced_king_positions__center(self):
        result = [(2, 1), (0, 1), (1, 2), (1, 0), (2, 2), (0, 2), (2, 0),
                  (0, 0)]
        assert pieces.get_menaced_king_positions((1, 1), 3, 3) == result

    def test_menaced_king_positions__right_bottom_corner(self):
        result = [(1, 2), (2, 1), (1, 1)]
        assert pieces.get_menaced_king_positions((2, 2), 3, 3) == result


class TestRook:
    def test_menaced_rook_positions__left_top_corner(self):
        result = [(1, 0), (2, 0), (0, 1), (0, 2)]
        assert pieces.get_menaced_rook_positions((0, 0), 3, 3) == result

    def test_menaced_rook_positions__center(self):
        result = [(2, 1), (0, 1), (1, 2), (1, 0)]
        assert pieces.get_menaced_rook_positions((1, 1), 3, 3) == result

    def test_menaced_rook_positions__right_bottom_corner(self):
        result = [(1, 2), (0, 2), (2, 1), (2, 0)]
        assert pieces.get_menaced_rook_positions((2, 2), 3, 3) == result


class TestBishop:
    def test_menaced_bishop_positions__left_top_corner(self):
        result = [(1, 1), (2, 2)]
        assert pieces.get_menaced_bishop_positions((0, 0), 3, 3) == result

    def test_menaced_bishop_positions__center(self):
        result = [(0, 0), (2, 0), (0, 2), (2, 2)]
        assert pieces.get_menaced_bishop_positions((1, 1), 3, 3) == result

    def test_menaced_bishop_positions__right_bottom_corner(self):
        result = [(1, 1), (0, 0)]
        assert pieces.get_menaced_bishop_positions((2, 2), 3, 3) == result
