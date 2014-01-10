#!/usr/bin/env python
""" Tufts Comp 131 Konane Skeleton

Play a game of Konane between two players, either of whom can be 1) Human 
2) Random or 3) An AI of your construction!

Usage:
  ./konane.py [-r <rows>] [-c <cols>] [-1 <p1type>] [-2 <p2type>] [--depth1=<p1depth>] [--depth2=<p2depth>]

Options:
  -1 <p1type>                 Sets the player type ([H]uman, [R]andom, or [M]inimax) for player 1.  [default: R]
  -2 <p2type>                 Sets the player type for player 2.  [default: R]
  -c <cols>, --cols=<cols>    Sets the number of columns on the board.  [default: 10]
  --depth1=<p1depth>          Sets the maximum depth for player 1.  [default: 4]
  --depth2=<p2depth>          Sets the maximum depth for player 2.  [default: 4]
  -h --help                   Show this screen.
  -r <rows>, --rows=<rows>    Sets the number of rows on the board.  [default: 10]
  -v                          Verbose mode.
"""

from docopt import docopt













def getLegalMoves(curBoard, player):
  pass

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
  # print arguments["--rows"]
