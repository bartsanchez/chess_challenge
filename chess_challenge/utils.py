PIECES = ['K', 'R']


def are_valid_pieces(pieces):
    """Return True if pieces as argument are valid or False otherwise."""
    return all([p in PIECES for p in pieces])
