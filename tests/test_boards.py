import unittest
from board import Board

class TestBoard(unittest.TestCase):

  def setUp(self):
    self.board = Board()

  def testInitialBoard(self):
    self.assertEqual(self.board.boardValues, ["_"]*9)

  def testSwapPlayers(self):
    self.board.currentPlayer = "X"
    self.board.swapPlayers()
    self.assertEqual(self.board.currentPlayer, "O")

  def testStartingPlayer(self):
    self.board.startingPlayer()
    potentialValues = ("X", "O")
    self.assertIn(self.board.currentPlayer, potentialValues)

  def testCheckWinTooEarly(self):
    self.board.turn = 3
    self.board.boardValues = ["X"] * 9
    hasWon = self.board.checkWin("X")
    self.assertEqual(False, hasWon)

  def testCheckWinHorizontal(self):
    self.board.turn = 9
    self.board.boardValues = ["_","_","_","_","_","_","X","X","X"]
    hasWon = self.board.checkWin("X")
    self.assertEqual(True, hasWon)

  def testCheckWinVertical(self):
    self.board.turn = 9
    self.board.boardValues = ["_","_","X","_","_","X","_","_","X"]
    hasWon = self.board.checkWin("X")
    self.assertEqual(True, hasWon)

  def testCheckWinDiagonal(self):
    self.board.turn = 9
    self.board.boardValues = ["_","_","X","_","X","_","X","_","_"]
    hasWon = self.board.checkWin("X")
    self.assertEqual(True, hasWon)

  def testCheckWinNone(self):
    self.board.turn = 9
    self.board.boardValues = ["_","X","X","X","_","X","X","X","_"]
    hasWon = self.board.checkWin("X")
    self.assertEqual(False, hasWon)

  def testCheckWinDifferentPlayer(self):
    self.board.turn = 9
    self.board.boardValues = ["X"] * 9
    hasWon = self.board.checkWin("O")
    self.assertEqual(False, hasWon)

  def testAIMoveOptimalStartingMoveGoFirst(self):
    self.board.aiPlayer = "O"
    self.board.humanPlayer = "X"
    self.board.currentPlayer = self.board.aiPlayer
    self.board.depth = 9
    optimalMove = (["O","_","_","_","_","_","_","_","_"],["_","_","O","_","_","_","_","_","_"],["_","_","_","_","_","_","O","_","_"],["_","_","_","_","_","_","_","_","O"])
    self.board.aiMoveSelect()
    self.assertIn(self.board.boardValues,optimalMove)

  def testAIMoveOptimalStartingMoveGoSecond(self):
    self.board.aiPlayer = "O"
    self.board.humanPlayer = "X"
    self.board.currentPlayer = self.board.aiPlayer
    self.board.depth = 9
    self.board.boardValues = ["X","_","_","_","_","_","_","_","_"]
    self.board.aiMoveSelect()
    self.assertEqual(self.board.boardValues,["X","_","_","_","O","_","_","_","_"])

  def testAIMoveStopLoss(self):
    self.board.aiPlayer = "O"
    self.board.humanPlayer = "X"
    self.board.currentPlayer = self.board.aiPlayer
    self.board.depth = 9
    self.board.turn = 5
    self.board.boardValues = ["X","X","_","O","_","_","O","_","_"]
    self.board.aiMoveSelect()
    self.assertEqual(self.board.boardValues,["X","X","O","O","_","_","O","_","_"])

  def testAIMoveGoForWin(self):
    self.board.aiPlayer = "O"
    self.board.humanPlayer = "X"
    self.board.currentPlayer = self.board.aiPlayer
    self.board.depth = 9
    self.board.turn = 5
    self.board.boardValues = ["O","O","_","X","_","_","X","_","_"]
    self.board.aiMoveSelect()
    self.assertEqual(self.board.boardValues,["O","O","O","X","_","_","X","_","_"])