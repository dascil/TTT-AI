class Board:
    def __init__(self):
        self.boardValues = ["_"] * 9
        self.currentPlayer = ""

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