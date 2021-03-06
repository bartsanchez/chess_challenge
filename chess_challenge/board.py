"""
Board related functions.
"""


def get_coordinates_from_board(rows, cols):
    """Returns an generator with all coordinates from a board."""
    for j in range(cols):
        for i in range(rows):
            yield (i, j)
