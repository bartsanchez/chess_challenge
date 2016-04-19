"""
Pieces functions.
"""


def get_menaced_positions(piece, position, rows, cols):
    """Determine the function to call for a given piece."""
    PIECES_FUNCTIONS = {
        'K': get_menaced_king_positions,
    }
    return PIECES_FUNCTIONS[piece](piece, position, rows, cols)


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
