#!/usr/bin/env python
"""
"""

from game_rules import linearizeBoard
from player import Player
from subprocess import Popen
from tempfile import TemporaryFile
from threading import Timer

import re

class ExternalPlayer(Player):
  def __init__(self, executable, symbol, timeout):
    super(ExternalPlayer, self).__init__(symbol)
    self.executable = executable
    self.timeout = timeout

  def selectInitialX(self, board):
    return _sanitizedMove(board)

  def selectInitialO(self, board):
    return _sanitizedMove(board)

  def getMove(self, board):
    return _sanitizedMove(board)

  def _sanitizedMove(board):
    legalMoves = game_rules.getLegalMoves(board, self.symbol)
    resultMove = _parseMove(_run(board))
    if resultMove in legalMoves:
      return resultMove
    else:
      return ((1, 2), (3, 4))

  def _run(board):
    tempOut = TemporaryFile(mode="w+")
    process = Popen([self.executable, "-p", self.symbol, "-r", len(board), "-c", len(board[0]), linearizeBoard(board)]
                    , stdout=tempOut)
    def killProcess():
      if process.poll() == None:
        try:
          process.kill()
          print('Error: process taking too long to complete--terminating')
        except:
          pass  # if the process exits between the poll and the kill, that's fine, do nothing
    timer = Timer(self.timeout, killProcess)
    timer.start()
    process.wait()
    timer.cancel()
    tempOut.seek(0)
    return tempOut.read()

  def _parseMove(move):
    return _parseInitialMove(move) or _parseSubsequentMove(move)

  def _parseInitialMove(move):
    match = re.match(r"^\((\d+), (\d+)\)$", move)
    return (int(match.group(1)), int(match.group(2))) if match else None

  def _parseSubsequentMove(move):
    match = re.match(r"^\(\((\d+), (\d+)\), \((\d+), (\d+)\)\)$", move)
    return ((int(match.group(1)), int(match.group(2)))
            , (int(match.group(3)), int(match.group(4)))) if match else None
