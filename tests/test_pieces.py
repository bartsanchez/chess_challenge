import mock

from chess_challenge import pieces


class TestMenacedPositionsCalls:
    @mock.patch('chess_challenge.pieces.get_menaced_bishop_positions')
    def test_calling_bishop(self, bishop_mock):
        pieces.get_menaced_positions('B', (0, 0), 3, 3)
        bishop_mock.assert_called_once_with((0, 0), 3, 3)

    @mock.patch('chess_challenge.pieces.get_menaced_queen_positions')
    def test_calling_queen(self, queen_mock):
        pieces.get_menaced_positions('Q', (0, 0), 3, 3)
        queen_mock.assert_called_once_with((0, 0), 3, 3)

    @mock.patch('chess_challenge.pieces.get_menaced_knight_positions')
    def test_calling_knight(self, knight_mock):
        pieces.get_menaced_positions('N', (0, 0), 3, 3)
        knight_mock.assert_called_once_with((0, 0), 3, 3)


class TestKing:
    def test_menaced_king_positions__left_top_corner(self):
        result = set([(1, 0), (0, 1), (1, 1)])
        assert pieces.get_menaced_king_positions((0, 0), 3, 3) == result

    def test_menaced_king_positions__center(self):
        result = set([(2, 1), (0, 1), (1, 2), (1, 0), (2, 2), (0, 2), (2, 0),
                      (0, 0)])
        assert pieces.get_menaced_king_positions((1, 1), 3, 3) == result

    def test_menaced_king_positions__right_bottom_corner(self):
        result = set([(1, 2), (2, 1), (1, 1)])
        assert pieces.get_menaced_king_positions((2, 2), 3, 3) == result


class TestRook:
    def test_menaced_rook_positions__left_top_corner(self):
        result = set([(1, 0), (2, 0), (0, 1), (0, 2)])
        assert pieces.get_menaced_rook_positions((0, 0), 3, 3) == result

    def test_menaced_rook_positions__center(self):
        result = set([(2, 1), (0, 1), (1, 2), (1, 0)])
        assert pieces.get_menaced_rook_positions((1, 1), 3, 3) == result

    def test_menaced_rook_positions__right_bottom_corner(self):
        result = set([(1, 2), (0, 2), (2, 1), (2, 0)])
        assert pieces.get_menaced_rook_positions((2, 2), 3, 3) == result


class TestBishop:
    def test_menaced_bishop_positions__left_top_corner(self):
        result = set([(1, 1), (2, 2)])
        assert pieces.get_menaced_bishop_positions((0, 0), 3, 3) == result

    def test_menaced_bishop_positions__center(self):
        result = set([(0, 0), (2, 0), (0, 2), (2, 2)])
        assert pieces.get_menaced_bishop_positions((1, 1), 3, 3) == result

    def test_menaced_bishop_positions__right_bottom_corner(self):
        result = set([(1, 1), (0, 0)])
        assert pieces.get_menaced_bishop_positions((2, 2), 3, 3) == result


class TestQueen:
    def test_menaced_queen_positions__left_top_corner(self):
        result = set([(1, 0), (2, 0), (0, 1), (0, 2), (1, 1), (2, 2)])
        assert pieces.get_menaced_queen_positions((0, 0), 3, 3) == result

    def test_menaced_queen_positions__center(self):
        result = set([(2, 1), (0, 1), (1, 2), (1, 0), (0, 0), (2, 0), (0, 2),
                      (2, 2)])
        assert pieces.get_menaced_queen_positions((1, 1), 3, 3) == result

    def test_menaced_queen_positions__right_bottom_corner(self):
        result = set([(1, 2), (0, 2), (2, 1), (2, 0), (1, 1), (0, 0)])
        assert pieces.get_menaced_queen_positions((2, 2), 3, 3) == result


class TestKnight:
    def test_menaced_knight_positions__left_top_corner(self):
        result = set([(1, 2), (2, 1)])
        assert pieces.get_menaced_knight_positions((0, 0), 3, 3) == result

    def test_menaced_knight_positions__center(self):
        result = set([])
        assert pieces.get_menaced_knight_positions((1, 1), 3, 3) == result

    def test_menaced_knight_positions__center__5x5(self):
        result = set([(3, 4), (4, 3), (4, 1), (3, 0), (1, 0), (0, 1), (0, 3),
                      (1, 4)])
        assert pieces.get_menaced_knight_positions((2, 2), 5, 5) == result

    def test_menaced_knight_positions__right_bottom_corner(self):
        result = set([(1, 0), (0, 1)])
        assert pieces.get_menaced_knight_positions((2, 2), 3, 3) == result
