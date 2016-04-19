"""
Utils functions.
"""

import itertools

PIECES = ['K', 'R']


def are_valid_pieces(pieces):
    """Return True if pieces as argument are valid or False otherwise."""
    return all([p in PIECES for p in pieces])


def get_pieces_combinations(pieces):
    """Return all permutations without repetitions for a set of pieces."""
    return set(list(itertools.permutations(pieces)))
