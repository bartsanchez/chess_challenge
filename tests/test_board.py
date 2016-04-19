from chess_challenge import board


class TestBoard:
    def test_get_coordinates_from_board__1x1(self):
        assert list(board.get_coordinates_from_board(1, 1)) == [(0, 0)]

    def test_get_coordinates_from_board__2x2(self):
        result = [(0, 0), (0, 1), (1, 0), (1, 1)]
        assert list(board.get_coordinates_from_board(2, 2)) == result

    def test_get_coordinates_from_board__3x2(self):
        result = [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)]
        assert list(board.get_coordinates_from_board(3, 2)) == result

    def test_get_coordinates_from_board__2x3(self):
        result = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)]
        assert list(board.get_coordinates_from_board(2, 3)) == result
