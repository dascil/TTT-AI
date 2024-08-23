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