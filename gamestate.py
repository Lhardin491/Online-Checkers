from board import *

class GameState:
    def __init__(self):
        self.board = Board()
        self.board.set_red_pieces()
        self.board.set_black_pieces()
        self.valid_moves = []

    def gen_valid_moves(self, x, y):
        self.valid_moves = self.board.get_valid_moves(x, y)
       
    def get_ghosts(self):
        return self.valid_moves

    def get_checkers(self):
        return [x for x in self.board.pieces.values()]
