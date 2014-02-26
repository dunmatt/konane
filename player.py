#!/usr/bin/env python
"""Tufts Comp 131 Stand Alone Konane Player

Running this file directly computes a single turn for the specified player.

Usage:
  ./player.py (-p <player>) [-t <type>] (-r <rows>) (-c <cols>) <board>

Options:
  -p <player>     Which player (x or o) the player is playing for?
  -t <type>       What player type for this player?  [default: M]
  -r <rows>       Sets the number of rows of the board.
  -c <cols>       Sets the number of columns of the board.
"""

import game_rules
import random

###########################################################################
# Explanation of the types:
# The board is represented by a row-major 2D list of characters, 0 indexed
# A point is a tuple of (int, int) representing (row, column)
# A move is a tuple of (point, point) representing (origin, destination)
# A jump is a move of length 2
###########################################################################

class Player(object):
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
  def __init__(self, symbol):
    super(MinimaxPlayer, self).__init__(symbol)

  def selectInitialX(self, board):
    return (0, 0)

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
    validMoves = game_rules.getFirstMovesForX(board)
    return random.choice(list(validMoves))

  def selectInitialO(self, board):
    validMoves = game_rules.getFirstMovesForO(board)
    return random.choice(list(validMoves))

  def getMove(self, board):
    mine = [(r, c) for r in range(len(board)) for c in range(len(board[0])) if game_rules.pieceAt(board, (r, c)) == self.symbol]
    allMoves = [(o, d) for o in mine for d in game_rules.getEmptySquares(board)]
    legalMoves = list(filter(lambda move: game_rules.isLegalMove(board, self.symbol, move, False), allMoves))
    if len(legalMoves) > 0:
      return random.choice(legalMoves)
    else:
      return ((0, 1), (2, 3))


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
    origin = self._promptForPoint("Choose a piece to move for %s (in the format 'row column'): " % self.symbol.capitalize())
    destination = self._promptForPoint("Choose a destination for %s (%s, %s) -> " % (self.symbol.capitalize(), origin[0], origin[1]))
    return (origin, destination)


def callMoveFunction(player, board):
  if game_rules.isInitialMove(board):
    if player.symbol == 'x':
      return player.selectInitialX(board)
    else:
      return player.selectInitialO(board)
  else:
    return player.getMove(board)

if __name__ == "__main__":
  # parse the arguments
  from docopt import docopt
  args = docopt(__doc__, version="Konane Player v1.0")
  # create a Player
  from konane import makePlayer
  player = makePlayer(args["-t"], args["-p"])
  # create a board
  rows = int(args["-r"])
  cols = int(args["-c"])
  board = game_rules.delinearizeBoard(args["<board>"], rows, cols)
  # call the appropriate select move function
  print(callMoveFunction(player, board))
