def get_coordinates_from_board(rows, cols):
    """Returns an generator with all coordinates from a board."""
    for i in range(rows):
        for j in range(cols):
            yield (i, j)
