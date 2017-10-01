from board import *


board = Board()
board.set_red_pieces()
board.set_black_pieces()
for i in range(8):
    for j in range(8):
        print(board.get_valid_moves(i, j))
print(board.pieces)
