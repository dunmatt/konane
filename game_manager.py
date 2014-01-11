#!/usr/bin/env python

from copy import deepcopy
import game_rules

# Game stage constants
AWAITING_INITIAL_X = -1
AWAITING_INITIAL_O = 0
X_TURN = 1
O_TURN = 2
X_VICTORY = 3
O_VICTORY = 4

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
    while self.stage is not X_VICTORY and self.stage is not O_VICTORY:
      self._takeTurn()

  def _takeTurn(self):
    playerBoard = deepcopy(self.board)
    if self.stage == AWAITING_INITIAL_X:
      self._handleInitialX(playerBoard, self.board)
    elif self.stage == AWAITING_INITIAL_O:
      self._handleInitialO(playerBoard, self.board)
    elif self.stage == X_TURN:
      self._handleTurnX(playerBoard, self.board)
    elif self.stage == O_TURN:
      self._handleTurnO(playerBoard, self.board)

  def _handleInitialX(self, playerBoard, board):
    pt = self.p1.selectInitialX(playerBoard)
    if pt in game_rules.getFirstMovesForX(board):
      self.board[pt[0]][pt[1]] = " "
      self.stage = AWAITING_INITIAL_O
    else:
      self.stage = O_VICTORY

  def _handleInitialO(self, playerBoard, board):
    pt = self.p2.selectInitialO(playerBoard)
    if pt in game_rules.getFirstMovesForO(board):
      self.board[pt[0]][pt[1]] = " "
      self.stage = X_TURN
    else:
      self.stage = X_VICTORY

  def _handleTurnX(self, playerBoard, board):
    print "xs turn"
    self.stage = O_TURN
    (self.board, legal) = game_rules.makePlayerMove(board, 'x', self.p1.getMove(playerBoard))
    if not legal:
      self.stage = O_VICTORY

  def _handleTurnO(self, playerBoard, board):
    self.stage = X_TURN
    (self.board, legal) = game_rules.makePlayerMove(board, 'o', self.p2.getMove(playerBoard))
    if not legal:
      self.stage = X_VICTORY
