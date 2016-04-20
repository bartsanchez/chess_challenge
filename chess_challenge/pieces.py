"""
Pieces functions.
"""

from chess_challenge import board


def get_menaced_positions(piece, position, rows, cols):
    """Determine the function to call for a given piece."""
    pieces_functions = {
        'K': get_menaced_king_positions,
        'R': get_menaced_rook_positions,
        'B': get_menaced_bishop_positions,
        'Q': get_menaced_queen_positions,
        'N': get_menaced_knight_positions,
    }
    return pieces_functions[piece](position, rows, cols)


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

    if current_i + 1 < rows and current_j + 1 < cols:
        result.append((current_i + 1, current_j + 1))

    if current_i - 1 >= 0 and current_j + 1 < cols:
        result.append((current_i - 1, current_j + 1))

    if current_i + 1 < rows and current_j - 1 >= 0:
        result.append((current_i + 1, current_j - 1))

    if current_i - 1 >= 0 and current_j - 1 >= 0:
        result.append((current_i - 1, current_j - 1))

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


def get_menaced_bishop_positions(position, rows, cols):
    """Return all menaced positions by a bishop."""
    result = []

    positions = list(board.get_coordinates_from_board(rows, cols))

    current_i, current_j = position
    while (current_i - 1, current_j - 1) in positions:
        current_i -= 1
        current_j -= 1
        result.append((current_i, current_j))

    current_i, current_j = position
    while (current_i + 1, current_j - 1) in positions:
        current_i += 1
        current_j -= 1
        result.append((current_i, current_j))

    current_i, current_j = position
    while (current_i - 1, current_j + 1) in positions:
        current_i -= 1
        current_j += 1
        result.append((current_i, current_j))

    current_i, current_j = position
    while (current_i + 1, current_j + 1) in positions:
        current_i += 1
        current_j += 1
        result.append((current_i, current_j))

    return result


def get_menaced_queen_positions(position, rows, cols):
    """Return all menaced positions by a queen."""
    return (
        get_menaced_rook_positions(position, rows, cols) +
        get_menaced_bishop_positions(position, rows, cols)
    )


def get_menaced_knight_positions(position, rows, cols):
    """Return all menaced positions by a knight."""
    result = []

    positions = list(board.get_coordinates_from_board(rows, cols))

    values = [
        (position[0] + 1, position[1] + 2),
        (position[0] + 2, position[1] + 1),
        (position[0] + 2, position[1] - 1),
        (position[0] + 1, position[1] - 2),
        (position[0] - 1, position[1] - 2),
        (position[0] - 2, position[1] - 1),
        (position[0] - 2, position[1] + 1),
        (position[0] - 1, position[1] + 2),
    ]

    for value in values:
        if value in positions:
            result.append(value)

    return result
