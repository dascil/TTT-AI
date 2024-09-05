from board import Board
import TextChecker

def TTT_AI():
    print("Welcome to Tic-Tac-Toe")
    game = Board()
    # Decide who goes first
    # Initiate Game
    # Keep going until an exit state is found
    # Prompt user to choose if they want to play again
    TextChecker.chooseGamePiece()
    game.setPlayers(userInput)
    print("Lets see who goes first")
    game.startingPlayer()
    if game.currentPlayer == game.humanPlayer:
        print("You will go first")
    else:
        print("I will go first")
    while True:
        game.turn += 1
        game.printCurrentBoard()
        if game.turn == game.GAME_END:
            print("It is a draw.")
            break

        if game.currentPlayer == game.humanPlayer:
            print("Please pick an available move")
            userInput = input()
            game.boardValues[int(userInput)-1] = game.humanPlayer

        else:
            print("My turn...")
            game.aiMoveSelect()

        if game.checkWin(game.currentPlayer):
            winMessage = "I win!" if game.currentPlayer == game.aiPlayer else "You win."
            game.printCurrentBoard()
            print(winMessage)
            break

        game.currentPlayer = game.humanPlayer if game.currentPlayer == game.aiPlayer else game.aiPlayer


if __name__ == "__main__":
    TTT_AI()