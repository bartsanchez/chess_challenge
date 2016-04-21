"""
Utils functions.
"""

import itertools

from repoze.lru import lru_cache

PIECES = ['K', 'R', 'B', 'Q', 'N']


def are_valid_pieces(pieces):
    """Return True if pieces as argument are valid or False otherwise."""
    return all([p in PIECES for p in pieces])


def get_pieces_combinations(pieces):
    """Return all permutations without repetitions for a set of pieces."""
    return set(list(itertools.permutations(pieces)))


@lru_cache(maxsize=500)
def get_next_position(i, j, rows, cols):
    """Return the next position in the board if available, False otherwise."""
    if i + 1 < rows:
        return (i + 1, j)
    elif j + 1 < cols:
        return (0, j + 1)
    else:
        return False, False
