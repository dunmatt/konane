#!/usr/bin/env python

import game_rules

class GameManager:
  def __init__(self, rows, cols, player1, player2):
    self.p1 = player1
    self.p2 = player2
    self.board = game_rules.makeBoard(rows, cols)