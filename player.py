#!/usr/bin/env python

import game_rules
import random

class Player:
  """ This is the player interface that is consumed by the GameManager.
  """
  def __init__(self, symbol):
    self.symbol = symbol  # 'x' or 'o'

  def selectInitialX(self, board):
    return (0, 0)

  def selectInitialO(self, board):
    pass

  def getMove(self, board):
    pass


class MinimaxPlayer(Player):
  def __init__(self, symbol, depth):
    super(MinimaxPlayer, self).__init__(symbol)
    self.depthLimit = depth

  def selectInitialX(self, board):
    # TODO: write me
    pass

  def selectInitialO(self, board):
    # TODO: write me
    pass

  def getMove(self, board):
    # TODO: write me
    pass


class RandomPlayer(Player):
  def __init__(self, symbol):
    super(RandomPlayer, self).__init__(symbol)

  def selectInitialX(self, board):
    # TODO: write me
    pass

  def selectInitialO(self, board):
    # TODO: write me
    pass

  def getMove(self, board):
    # TODO: write me
    pass


class HumanPlayer(Player):
  def __init__(self, symbol):
    super(HumanPlayer, self).__init__(symbol)

  def _promptForPoint(self, prompt):
    raw = raw_input(prompt)
    (r, c) = raw.split()
    return (int(r), int(c))

  def selectInitialX(self, board):
    game_rules.printBoard(board)
    pt = (0, 0, 0)  # obviously not a valid location on a 2-D board
    validMoves = game_rules.getFirstMovesForX(board)
    while pt not in validMoves:
      pt = self._promptForPoint("Enter a valid starting location for player X (in the format 'row column'): ")
    return pt

  def selectInitialO(self, board):
    game_rules.printBoard(board)
    pt = (0, 0, 0)  # obviously not a valid location on a 2-D board
    validMoves = game_rules.getFirstMovesForO(board)
    while pt not in validMoves:
      pt = self._promptForPoint("Enter a valid starting location for player O (in the format 'row column'): ")
    return pt

  def getMove(self, board):
    game_rules.printBoard(board)
    origin = self._promptForPoint("Choose a piece to move for %s (in the format 'row column'): " % self.symbol)
    destination = self._promptForPoint("Choose a destination for %s (%s, %s) -> " % (self.symbol, origin[0], origin[1]))
    return (origin, destination)
