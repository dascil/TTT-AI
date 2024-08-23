from board import Board

def TTT_AI():
    print("Welcome to Tic-Tac-Toe")
    game = Board()
    print("Would you like to be X or O?")
    # Prompt user to pick X or O
    # Decide who goes first
    # Initiate Game
    # Keep going until an exit state is found
    # Prompt user to choose if they want to play again
    userInput = input()
    print("You will be {}".format(userInput))
    game.humanPlayer = "X"
    game.aiPlayer= "O"
    print("Lets see who goes first")
    game.startingPlayer()
    if game.currentPlayer == game.humanPlayer:
        print("You will go first")
    else:
        print("I will go first")
    while True:
        game.turn += 1
        game.printCurrentBoard()
        if game.turn == 10:
            print("It is a draw.")
            break
        if game.currentPlayer == game.humanPlayer:
            print("Please pick an available move")
            userInput = input()
            game.boardValues[int(userInput)-1] = game.humanPlayer
            win = game.checkWin(game.humanPlayer)
            print(win)
            if win:
                game.printCurrentBoard()
                print("You win.")
                break
        if game.currentPlayer == game.aiPlayer:
            print("My turn...")
            game.aiMoveSelect()
            win = game.checkWin(game.humanPlayer)
            if win:
                game.printCurrentBoard()
                print("I win!")
                break
        game.currentPlayer = game.humanPlayer if game.currentPlayer == game.aiPlayer else game.aiPlayer


if __name__ == "__main__":
    TTT_AI()