#!/usr/bin/python3
"""N-Queen puzzle using backtracking"""


def safeSpot(queenPosition, queenN):
    """Safe spot checker
    Args:
        queenPosition: Array with queens positions
        queenN: Amount of queens"""
    for i in range(queenN):
        if queenPosition[i] == queenPosition[queenN]:
            return False
        if abs(queenPosition[i] - queenPosition[queenN]) == abs(i - queenN):
            return False
    return True


def locateQueens(queenPosition, queenNumber):
    """Prints the list with the Queens positions
    Args:
        queenPosition: Array with queens positions
        queenNumber: amount of queens"""
    queens = []
    for i in range(queenNumber):
        queens.append([i, queenPosition[i]])
    print(queens)


def Queen(queenPosition, queenNumber):
    """Backtracking algorithm
    Args:
        queenPosition: Array with queens positions
        queenNumber: amount of queens"""
    if queenNumber is len(queenPosition):
        locateQueens(queenPosition, queenNumber)
        return
    queenPosition[queenNumber] = -1
    while((queenPosition[queenNumber] < len(queenPosition) - 1)):
        queenPosition[queenNumber] += 1
        if safeSpot(queenPosition, queenNumber) is True:
            if queenNumber is not len(queenPosition):
                Queen(queenPosition, queenNumber + 1)


def solveNQueen(size):
    """Function that applies backtracking algorithm
    Args:
        size: size of the chessboard"""
    queenPosition = [-1 for i in range(size)]
    Queen(queenPosition, 0)


if __name__ == '__main__':
    import sys
    if len(sys.argv) == 1 or len(sys.argv) > 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        size = int(sys.argv[1])
    except(TypeError, ValueError):
        print("N must be a number")
        sys.exit(1)
    if size < 4:
        print("N must be at least 4")
        sys.exit(1)
    solveNQueen(size)
