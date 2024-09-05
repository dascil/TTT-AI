import random as r



class Board:

    boardValues: list
    wins: list
    currentPlayer: str
    humanPlayer: str
    aiPlayer: str
    turn: int
    depth: int
    GAME_END = 10


    # Easy - Depth == 1-2
    # Medium - Depth == 3
    # Hard - Depth >= 5
    def __init__(self):
        self.boardValues = ["_"] * 9
        self.wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
        self.turn = 0
        self.depth = 3

    def setPlayers(self, humanPlayer):
        """
        Sets players for the board

        Arguments:
                humanPlayer: str
                The piece the player chose
        """
        self.humanPlayer = humanPlayer
        self.aiPlayer = "X" if humanPlayer == "O" else "X"

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

    def checkWin(self, player):
        """
        Check through every board combination to see if a win condition has happened
        """
        # Can't achieve a win if less than two moves by player happened
        if self.turn < 5:
            return False
        # Checks all available wins
        for win in self.wins:
            # Checks to see if all indices match the current player in the array
            winFound = True
            for indice in win:
                if self.boardValues[indice]  != player:
                    winFound = False
            if winFound:
                return True

        return False

    def aiMoveSelect(self):
        """
        Picks the best move for the AI
        """
        (_, moves) = self.minimax(True, 0)
        index = r.choice(moves)
        self.boardValues[index] = self.aiPlayer

    # TODO: Implement alpha beta pruning and add a heuristic
    def minimax(self, isMax, depth, alpha=float('-inf'), beta=float('inf')):
        """
        Minimax algorithm with alpha beta pruning for TTT AI

        Arguments:
                isMax : boolean
                    Is current level trying to minimize or maximize value
                depth: integer
                    How far to look ahead
                alpha: integer
                    Minimum score for maximizing player
                beta: integer
                    Maximum score for minimizing player
        Returns:
                value: integer
                    The sum of values of either the node itself or its subtrees
        """

        # Check if AI won during this move
        if isMax:
            if self.checkWin(self.aiPlayer):
                return (1, -1)

        # Check if human player one during this move
        else:
            if self.checkWin(self.humanPlayer):
                return (-1, -1)

        # If draw or reached end of lookahead
        if self.turn == 10 or depth == self.depth:
            return (0,-1)

        # Variables for return values
        optimalValue =  float("-inf") if isMax else float("inf")
        optimalMoves = []


        for index, value in enumerate(self.boardValues):
            # Index already used
            if value != "_":
                continue

            # Increment for recursion
            self.turn += 1

            # Recurses into branch and will either optimal value, add to set, or skip the results
            if isMax:
                self.boardValues[index] = self.aiPlayer
                potentialValue, _= self.minimax(False, depth+1)
                if potentialValue > optimalValue:
                    optimalValue = potentialValue
                    optimalMoves = [index]
                elif potentialValue == optimalValue:
                    optimalMoves.append(index)


            else:
                self.boardValues[index] = self.humanPlayer
                potentialValue, _= self.minimax(True, depth+1)
                if potentialValue < optimalValue:
                    optimalValue = potentialValue
                    optimalMoves = [index]
                elif potentialValue == optimalValue:
                    optimalMoves.append(index)


            # Undo changes to board
            self.boardValues[index] = "_"
            self.turn -= 1

        return optimalValue, optimalMoves
