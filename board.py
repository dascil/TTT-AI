import random as r

class Board:
    def __init__(self):
        self.boardValues = ["_"] * 9
        self.currentPlayer = ""
        self.wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]

    def startingPlayer(self):
        """
        Decides starting player for game
        """
        startingPlayer = r.randint(0,1)
        self.currentPlayer = "X" if startingPlayer == 0 else "O"

    def swapPlayers(self):
        """
        Changes currentPlayer to other player
        """
        self.currentPlayer = "X" if self.currentPlayer == "O" else "O"

    def printCurrentBoard(self):
        """
        Prints out the current game board.
        Takes in the values from boardValues.
        """
        print("-|-----|-----|-----|-")
        print(" |     |     |     | ")
        print(" |  {}  |  {}  |  {}  | ".format(self.boardValues[0], self.boardValues[1], self.boardValues[2]))
        print(" |     |     |     | ")
        print("-|-----|-----|-----|-")
        print(" |     |     |     | ")
        print(" |  {}  |  {}  |  {}  | ".format(self.boardValues[3], self.boardValues[4], self.boardValues[5]))
        print(" |     |     |     | ")
        print("-|-----|-----|-----|-")
        print(" |     |     |     | ")
        print(" |  {}  |  {}  |  {}  | ".format(self.boardValues[6], self.boardValues[7], self.boardValues[8]))
        print(" |     |     |     | ")
        print("-|-----|-----|-----|-")

    def printBoardIndexes(self):
        """
        Prints out the current game board.
        Takes in the values from boardValues.
        """
        print("-|-----|-----|-----|-")
        print(" |     |     |     | ")
        print(" |  1  |  2  |  3  | ")
        print(" |     |     |     | ")
        print("-|-----|-----|-----|-")
        print(" |     |     |     | ")
        print(" |  4  |  5  |  6  | ")
        print(" |     |     |     | ")
        print("-|-----|-----|-----|-")
        print(" |     |     |     | ")
        print(" |  7  |  8  |  9  | ")
        print(" |     |     |     | ")
        print("-|-----|-----|-----|-")