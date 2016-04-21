"""
Main functions.
"""
import collections

from chess_challenge import pieces as pieces_mod
from chess_challenge import utils


def solve(rows, cols, pieces):
    """Find all unique and valid configurations for the pieces in the board."""

    if not utils.are_valid_pieces(pieces):
        print 'The pieces passed as argument are not valid.'
        return -1

    solutions = collections.defaultdict(list)
    combinations = utils.get_pieces_combinations(pieces)
    for combination in combinations:
        # TODO: Implement concurrency here for lower the time spent
        solve_combination(
            combination=combination,
            original_combination=combination,
            i=0,
            j=0,
            rows=rows,
            cols=cols,
            occupied_positions=set(),
            menaced_positions=set(),
            solutions=solutions,
        )

    return solutions


def solve_combination(combination,
                      original_combination,
                      i,
                      j,
                      rows,
                      cols,
                      occupied_positions,
                      menaced_positions,
                      solutions):
    """Generates possible solutions for the given combination and the pos."""
    if not combination:
        solutions[original_combination].append(occupied_positions)
        return

    while i is not False and i < rows and j < cols:
        if (i, j) not in menaced_positions:
            new_menaces = pieces_mod.get_menaced_positions(
                combination[0], (i, j), rows, cols,
            )
            if not occupied_positions.intersection(new_menaces):
                next_i, next_j = utils.get_next_position(i, j, rows, cols)
                new_menaces = pieces_mod.get_menaced_positions(
                    combination[0], (i, j), rows, cols,
                )
                solve_combination(
                    combination=combination[1:],
                    original_combination=original_combination,
                    i=next_i,
                    j=next_j,
                    rows=rows,
                    cols=cols,
                    occupied_positions=occupied_positions.union(set([(i, j)])),
                    menaced_positions=menaced_positions.union(new_menaces),
                    solutions=solutions,
                )
        (i, j) = utils.get_next_position(i, j, rows, cols)
