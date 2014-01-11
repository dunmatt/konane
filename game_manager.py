#!/usr/bin/env python

import game_rules

# Game stage constants
AWAITING_INITIAL_X = -1
AWAITING_INITIAL_O = 0
X_TURN = 1
Y_TURN = 2
X_VICTORY = 3
Y_VICTORY = 4

class GameManager:
  def __init__(self, rows, cols, player1, player2):
    self.rows = rows
    self.cols = cols
    self.p1 = player1
    self.p2 = player2
    self.stage = AWAITING_INITIAL_X
    self.reset()

  def reset(self):
    self.board = game_rules.makeBoard(self.rows, self.cols)

  def play(self):
    # TODO: write me
    pass
