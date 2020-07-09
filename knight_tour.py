"""
Abstract: The following code is used to solve the knight tour problem recursively.
Credits: Omar Hamza (https://github.com/omarmhamza)
"""

from chess import Board, Knight
import time



def solve(board, knight):
    """
    :param board: Takes in instance Board that moves the knight
    :param knight: Takes in instance of Knight
    :return: Solution for Knight tour for the specific instance of Knight
    """
    knight_moves = knight.getMovements()
    if board.goal(knight.numberOfMoves):
        return True
    for move in knight_moves:
        if board.isSafeMove(move):
            knight.setPosition(move[0], move[1])  # forward
            board.setMove(knight)
            if solve(board, knight):  # calling recursively
                return True
            knight.setPosition(move[0], move[1])  # backtrack
            board.resetMove(knight)
    return False


def searchForSolutions(boardXDim, boardYDim,SAVE=False,SHOW=False,DIRECTORY =""):
    """
    :param boardYDim: number of boxes in the Y axis
    :param boardXDim : number of boxes in the X axis
    :param DIRECTORY: Where to save the solution (PNG)
    :param SHOW: whether to show the solution (plot)
    :param SAVE: whether to save the solution (PNG)
    :returns prints solution for every position of the Knight on a chess board with boardXDim*boardYDim boxes
    """
    for i in range(boardXDim):
        for j in range(boardYDim):
            board = Board(boardXDim, boardYDim)
            board.SAVE = SAVE
            board.GRAPHICS = SHOW
            board.SAVE_SOLUTION_DICT = DIRECTORY
            knight = Knight(board, i, j)
            print("Setting knight at ", knight.getPosition())
            start = time.time()
            if solve(board, knight):
                print("Found solution")
                print("Time took: ", round(time.time() - start, 2), "second(s)")
                board.show(knight)
            else:
                print("No solution")


def solveOnce(board, knight):
    """

    :param board: takes in an instance of Board
    :param knight: takes in an instance of Knight
    :returns Prints knight tour solution with the time taken to solve it
    """
    start = time.time()
    if solve(board, knight):
        print("Found solution")
        print("Time took: ", round(time.time() - start, 2), "second(s)")
        board.show(knight)
    else:
        print("No solution")


