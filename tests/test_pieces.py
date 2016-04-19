from chess_challenge import pieces


class TestKing:
    def test_menaced_king_positions__left_top_corner(self):
        result = [(1, 0), (0, 1)]
        assert pieces.get_menaced_king_positions('K', (0, 0), 3, 3) == result

    def test_menaced_king_positions__center(self):
        result = [(2, 1), (0, 1), (1, 2), (1, 0)]
        assert pieces.get_menaced_king_positions('K', (1, 1), 3, 3) == result

    def test_menaced_king_positions__right_bottom_corner(self):
        result = [(1, 2), (2, 1)]
        assert pieces.get_menaced_king_positions('K', (2, 2), 3, 3) == result
