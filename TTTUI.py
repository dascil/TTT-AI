from board import Board

def initializeBoard():
    print("Welcome to Tic-Tac-Toe")
    return Board()

def chooseGamePiece(game:Board):
    validInput = False
    while not validInput:
        print("Would you like to be X or O?")
        userInput = str(input()).upper()
        validInput = checkValidPlayer(userInput)
        if not validInput:
            print("Your response is not valid.\nPlease type X or O.")
    print("You will be {}".format(userInput))
    game.setPlayers(userInput)

def checkValidPlayer(userInput:str):
    return userInput == "X" or userInput == "O"

def chooseWhoGoesFirst(game: Board):
    print("Lets see who goes first")
    game.startingPlayer()
    if game.currentPlayer == game.humanPlayer:
        print("You will go first")
    else:
        print("I will go first")