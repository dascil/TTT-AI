from board import Board
import re

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

def checkValidMoveInput(userInput: str):
    pattern = r'^[1-9]+$'
    return len(userInput) == 1 and re.match(pattern,userInput)

def humanMoveSelect(game: Board):
    validInput = False
    while not validInput:
        print("Please pick an available move")
        userInput = input()
        validInput = checkValidMoveInput(userInput)
        if not validInput:
            print("The choice you made is not in the correct format.\nPlease pick a value between 1-9.")
            continue
        userInput = int(userInput)-1
        if game.boardValues[userInput] != "_":
            validInput = False
            print("That spot is already in use.\nPlease pick a different spot.")
        else:
            game.boardValues[userInput] = game.humanPlayer

def chooseWhoGoesFirst(game: Board):
    print("Lets see who goes first")
    game.startingPlayer()
    if game.currentPlayer == game.humanPlayer:
        print("You will go first")
    else:
        print("I will go first")