from board import Board
import UI as ui

def TTT_AI():
    # Initiate Game
    # Keep going until an exit state is found
    # Prompt user to choose if they want to play again
    game = ui.initializeBoard()
    ui.chooseGamePiece(game)
    ui.chooseWhoGoesFirst(game)
    winFound = False
    while not winFound and game.turn < game.GAME_END:
        game.printCurrentBoard()

        if game.currentPlayer == game.humanPlayer:
            ui.humanMoveSelect(game)

        else:
            print("My turn...")
            game.aiMoveSelect()

        winFound = game.checkWin(game.currentPlayer)

        if not winFound:
            game.changeCurrentPlayer()

        game.incrementTurn()

    game.printCurrentBoard()

    if winFound:
        winMessage = "I win!" if game.currentPlayer == game.aiPlayer else "You win."
        print(winMessage)
    else:
        print("It is a draw.")


if __name__ == "__main__":
    TTT_AI()