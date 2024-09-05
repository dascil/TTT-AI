def chooseGamePiece():
    validInput = False
    while not validInput:
        print("Would you like to be X or O?")
        userInput = str(input()).upper()
        validInput = checkValidPlayer(userInput)
        if not validInput:
            print("Your response is not valid.\nPlease type X or O.")
    print("You will be {}".format(userInput))

def checkValidPlayer(userInput:str):
    return userInput == "X" or userInput == "O"
