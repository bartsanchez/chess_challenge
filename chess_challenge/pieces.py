"""
Pieces functions.
"""


def get_menaced_king_positions(piece, position, rows, cols):
    """Return all menaced position by a king."""
    result = []

    current_i, current_j = position

    if current_i + 1 < rows:
        result.append((current_i + 1, current_j))

    if current_i - 1 >= 0:
        result.append((current_i - 1, current_j))

    if current_j + 1 < cols:
        result.append((current_i, current_j + 1))

    if current_j - 1 >= 0:
        result.append((current_i, current_j - 1))

    return result
