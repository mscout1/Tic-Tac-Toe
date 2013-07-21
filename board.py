"""
The Tic Tac Toe Board

"""
from itertools import chain
from pprint import pformat

board_template ="""
 {0[0]} | {0[1]} | {0[2]}
-----------
 {1[0]} | {1[1]} | {1[2]}
-----------
 {2[0]} | {2[1]} | {2[2]}
"""

X='X'
O='O'
STALEMATE=EMPTY=' '

class Board(object):
    """docstring for ClassName"""
    def __init__(self):
        self._spaces = [[EMPTY]*3]*3

    def __repr__(self):
        return pformat(self._spaces)

    def __str__(self):
        return board_template.format(*self._spaces)

    def rows(self): #"yield from" is not available until 3.3
        return (tuple(row) for row in self._spaces)

    def cols(self):#"yield from" is not available until 3.3
        return (tuple(row) for row in zip(*self._spaces))

    def diags(self):
        yield (self._spaces[0][0], self._spaces[1][1], self._spaces[2][2])
        yield (self._spaces[2][0], self._spaces[1][1], self._spaces[0][2])

    def rows_cols_diags(self): #"yield from" is not available until 3.3
        return chain(self.rows(), self.cols(), self.diags())

    def play(self, player, row, col):
        assert self._spaces[row][col] == EMPTY
        self._spaces[row][col] = player

    def check_win(self):
        for rcd in self.rows_cols_diags():
            if (rcd[0] == rcd[1] == rcd[2]) and rcd[0] in (X,O):
                return rcd[0]
        for space in (c for r in self._spaces for c in r ):
            if space == EMPTY:
                break
        else:
            return STALEMATE
        return None







