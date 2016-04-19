"""
Pieces functions.
"""


def get_menaced_positions(piece, position, rows, cols):
    """Determine the function to call for a given piece."""
    PIECES_FUNCTIONS = {
        'K': get_menaced_king_positions,
        'R': get_menaced_rook_positions,
    }
    return PIECES_FUNCTIONS[piece](position, rows, cols)


def get_menaced_king_positions(position, rows, cols):
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


def get_menaced_rook_positions(position, rows, cols):
    """Return all menaced positions by a rook."""
    result = []

    current_i, current_j = position

    i = current_i
    while i + 1 < rows:
        i += 1
        result.append((i, current_j))

    i = current_i
    while i - 1 >= 0:
        i -= 1
        result.append((i, current_j))

    j = current_j
    while j + 1 < cols:
        j += 1
        result.append((current_i, j))

    j = current_j
    while j - 1 >= 0:
        j -= 1
        result.append((current_i, j))

    return result
