#!/usr/bin/env python

import game_rules
import random

class Player:
  """ This is the player interface that is consumed by the GameManager.
  """
  def __init__(self, symbol):
    self.symbol = symbol  # 'x' or 'o'

  def selectInitialX(self, board):
    pass

  def selectInitialO(self, board):
    pass

  def makeMove(self, board):
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

  def makeMove(self, board):
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

  def makeMove(self, board):
    # TODO: write me
    pass


class HumanPlayer(Player):
  def __init__(self, symbol):
    super(HumanPlayer, self).__init__(symbol)

  def selectInitialX(self, board):
    # TODO: write me
    pass

  def selectInitialO(self, board):
    # TODO: write me
    pass

  def makeMove(self, board):
    # TODO: write me
    pass
