#!/usr/bin/env python
"""
"""

from player import Player

class ExternalPlayer(Player):
  def __init__(self, executable, symbol):
    super(ExternalPlayer, self).__init__(symbol)
    self.executable = executable

  def selectInitialX(self, board):
    pass

  def selectInitialO(self, board):
    pass

  def getMove(self, board):
    pass