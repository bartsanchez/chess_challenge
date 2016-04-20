#!/usr/bin/env python2
import datetime

from chess_challenge import main as chess_main


def main():
    start = datetime.datetime.now()
    # result = chess_main.solve(3, 3, ['K', 'K', 'R'])
    # result = chess_main.solve(4, 4, ['R', 'R', 'N', 'N', 'N', 'N'])
    result = chess_main.solve(7, 7, ['K', 'K', 'Q', 'Q', 'B', 'B', 'N'])
    end = datetime.datetime.now()

    number_of_unique_combinations = sum([len(v) for v in result.values()])
    print 'Total unique configurations: {0}'.format(
        number_of_unique_combinations
    )
    print 'Time spent: {0}'.format(end - start)
    for combination, configurations in result.iteritems():
        print 'Combination: {0}'.format(combination)
        for configuration in configurations:
            print configuration


if __name__ == '__main__':
    main()
