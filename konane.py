#!/usr/bin/env python
""" Tufts Comp 131 Konane Skeleton

Play a game of Konane between two players, either of whom can be 1) Human 
2) Random or 3) An AI of your construction!

Usage:
  ./konane.py [-r <rows>] [-c <cols>] [-1 <p1type>] [-2 <p2type>] [--depth1=<p1depth>] [--depth2=<p2depth>] [-i <iter>]

Options:
  -1 <p1type>                      Sets the player type ([H]uman, [R]andom, or [M]inimax) for player 1.  [default: R]
  -2 <p2type>                      Sets the player type for player 2.  [default: R]
  -c <cols>, --cols=<cols>         Sets the number of columns on the board.  [default: 10]
  --depth1=<p1depth>               Sets the maximum depth for player 1.  [default: 4]
  --depth2=<p2depth>               Sets the maximum depth for player 2.  [default: 4]
  -h --help                        Show this screen.
  -r <rows>, --rows=<rows>         Sets the number of rows on the board.  [default: 10]
  -i <iter>, --iterations=<iter>   Sets the number of games to run.  [default: 1]
"""
  # -v                               Verbose mode.

###########################################################################
# Explanation of the types:
# The board is represented by a row-major 2D list of characters, 0 indexed
# A point is a tuple of (int, int) representing (row, column)
# A move is a tuple of (point, point) representing (origin, destination)
###########################################################################

from copy import deepcopy
from docopt import docopt
from itertools import izip

import math







def makeMove(board, move):
  if isLegalMove(board, pieceAt(move[0]), move):
    newBoard = deepcopy(board)
    for jump in interpolateMove(move):
      makeJump(newBoard, jump)
    return (newBoard, True)
  else:
    print "Illegal move, ignoring"
    return (board, False)

def makeJump(board, jump):
  mid = midPoint(jump)
  board[mid[0]][mid[1]] = " "
  board[jump[1][0]][jump[1][1]] = board[jump[0][0]][jump[0][1]]
  board[jump[0][0]][jump[0][1]] = " "

def moveLength(move):
  return math.abs(move[0][0] - move[1][0]) if verticalMove(move) else math.abs(move[0][1] - move[1][1])

def isLegalMove(board, player, move):
  if pieceAt(board, move[0]) != player:
    print "You can only move your own pieces"
    return False
  length = moveLength(move)
  if length % 2 == 1:
    print "Cannot move an odd number of squares"
    return False
  if length == 0:
    print "Cannot stay put"
    return False
  other = 'o' if player == 'x' else 'x'
  for jump in interpolateMove(move):
    if not isLegalJump(board, player, other, jump):
      print "Illegal move"
      return False
  return True

def isLegalJump(board, player, other, jump):
  return pieceAt(board, jump[0]) == player and pieceAt(board, midPoint(jump)) == other and pieceAt(board, jump[1]) == " "

def interpolateMove(move):
  rangeIndex = -1
  if horizontalMove(move):
    rangeIndex = 1
  elif verticalMove(move):
    rangeIndex = 0
  else:
    print "Cannot move diagonally"
    return []
  constIndex = 0 if rangeIndex else 1
  step = 2 if move[0][rangeIndex] < move[1][rangeIndex] else -2
  points = [(move[0][constIndex], c) for c in range(move[0][rangeIndex], move[1][rangeIndex] + step, step)]
  return izip(points, points[1:])

def midPoint(move):
  if horizontalMove(move):
    return (move[0][0], (move[0][1]+move[1][1])/2)
  elif verticalMove(move):
    return ((move[0][0]+move[1][0])/2, move[0][1])
  else:
    print "Cannot move diagonally"

def horizontalMove(move):
  return move[0][0] == move[1][0]

def verticalMove(move):
  return move[0][1] == move[1][1]

def pieceAt(board, point):
  return board[point[0]][board[point[1]]]

def onBoard(rows, cols, point):
  return 0 <= point[0] and point[0] < rows and 0 <= point[1] and point[1] < cols

def getNeighbors(board, point):
  rows = len(board)
  cols = len(board[0])
  return filter(lambda pt: onBoard(rows, cols, pt), [(point[0]-1, point[1])
                                                    , (point[0]+1, point[1])
                                                    , (point[0], point[1]-1)
                                                    , (point[0], point[1]+1)])

def getEmptySquares(board):
  return ((r, c) for r in range(len(board)) for c in range(len(board[0])) if board[r][c] == " ")

def printBoard(board):
  for row in board:
    print "".join(row)

if __name__ == "__main__":
  arguments = docopt(__doc__, version="Konane v1.0")
  rows = int(arguments["--rows"])
  cols = int(arguments["--cols"])
  board = [['x' if (r+c)%2 == 0 else 'o' for c in range(cols)] for r in range(rows)]
  printBoard(board)
  iterations = int(arguments["--iterations"])
  # TODO: run the game for the appropriate number of iterations
