"""
Main functions.
"""

import utils


def solve(rows, cols, pieces):
    """Find all unique and valid configurations for the pieces in the board."""

    if not utils.are_valid_pieces(pieces):
        print('The pieces passed as argument are not valid.')
        return -1

    return 0
