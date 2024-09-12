from board import Board
import TTTUI as ui

def TTT_AI():
    # Initiate Game
    # Keep going until an exit state is found
    # Prompt user to choose if they want to play again
    game = ui.initializeBoard()
    ui.chooseGamePiece(game)
    ui.chooseWhoGoesFirst(game)
    while True:
        game.incrementTurn()
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

        game.changeCurrentPlayer()


if __name__ == "__main__":
    TTT_AI()