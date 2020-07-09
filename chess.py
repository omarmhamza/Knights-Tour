import numpy as np
import matplotlib.pyplot as plt
from mlxtend.plotting import checkerboard_plot  # used for the graphical representation of the Chessboard (pip
# install mlxtend) Credits: https://rasbt.github.io/mlxtend/


class Board:
    def __init__(self, xDim, yDim):
        self.xDim = xDim
        self.yDim = yDim
        self.boxes = np.full(
            shape=(xDim, yDim),
            fill_value=-1,
            dtype=np.int)
        self.SAVE = 0
        self.GRAPHICS = 0
        self.SAVE_SOLUTION_DICT = ""

    def goal(self, numberOfMoves):  # returns True if the number of moves matches the total number of chess boxes
        return numberOfMoves == self.xDim * self.yDim

    def getXDim(self):
        return self.xDim

    def getYDim(self):
        return self.yDim

    def isSafeMove(self, position):  # checks if it is a safe position to go to
        return 0 <= position[0] < self.xDim and 0 <= position[1] < self.yDim and self.boxes[
            position[0], position[1]] == -1

    def setMove(self, knight):  # increments the number of moves of the Knight and places it on the board
        knight.numberOfMoves += 1
        self.boxes[knight.getPosition()] = knight.numberOfMoves

    def resetMove(self, knight):  # decrements the number of moves of the Knight and removes it from its position on
        # the board
        self.boxes[knight.getPosition()] = -1
        knight.numberOfMoves -= 1

    def show(self, knight):  # prints out an array of the boxes, if GRAPHICS is enabled a plot will be shown
        print(self.boxes)
        # the below sets up a chess board format and then shows chessboard plot using matplotlib

        if self.GRAPHICS or self.SAVE:
            ary = self.boxes
            alpha = 'a'
            col_labels = []
            row_labels = []
            for i in range(0, self.getYDim()):
                col_labels.append(alpha)
                row_labels.append(i + 1)
                alpha = chr(ord(alpha) + 1)
            checkerboard_plot(ary, fmt="%d", col_labels=col_labels, row_labels=row_labels)
        if self.SAVE:
            if self.SAVE_SOLUTION_DICT:
                plt.savefig("{}/plot_{}x{}_knight@{}{}".format(self.SAVE_SOLUTION_DICT, self.xDim, self.yDim,
                                                               str(knight.x_start), str(knight.y_start)))
                print(self.SAVE_SOLUTION_DICT)
            else:
                plt.savefig(
                    "plot_{}x{}_knight@{}{}".format(self.xDim, self.yDim, str(knight.x_start), str(knight.y_start)))
            print("Saved")
        if self.GRAPHICS:
            plt.show()


class Knight:
    def __init__(self, board, x_position, y_position):
        self.x_position = x_position
        self.x_start = x_position
        self.y_position = y_position
        self.y_start = y_position
        self.board = board
        self.numberOfMoves = 1
        board.boxes[x_position, y_position] = 1

    def getPosition(self):
        return self.x_position, self.y_position

    def setPosition(self, x, y):
        self.x_position = x
        self.y_position = y

    def getMovements(self):
        knight_moves = [
            (self.x_position + 2, self.y_position + 1),
            (self.x_position + 1, self.y_position + 2),
            (self.x_position - 1, self.y_position + 2),
            (self.x_position - 2, self.y_position + 1),
            (self.x_position - 2, self.y_position - 1),
            (self.x_position - 1, self.y_position - 2),
            (self.x_position + 1, self.y_position - 2),
            (self.x_position + 2, self.y_position - 1)
        ]
        return knight_moves
