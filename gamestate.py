from board import *
from genetics import *

class GameState:
    def __init__(self):
        self.num_strats = 6
        self.board = Board()
        self.board.set_red_pieces()
        self.board.set_black_pieces()
        self.valid_moves = []
        self.hitlist = []
        self.name = -1
        self.turn = "black"
        self.move_strats = [MovementStrategy()] * self.num_strats
        self.strat = 0

        for strat in self.move_strats:
            strat.generate()

    def is_valid(self, x, y):
        print (self.valid_moves)
        print (self.hitlist)
        try:
            print (self.valid_moves.index((x, y)))
            return self.hitlist[self.valid_moves.index((x, y))]
        except:
            return -2

    def do_stuff(self, x, y):
        if self.board.pieces.get((x, y)) is not None:
            self.name = self.board.pieces.get((x, y)).name
            self.valid_moves, self.hitlist = self.board.get_valid_moves(x, y)
       
    def get_ghosts(self):
        return self.valid_moves

    def get_checkers(self):
        return [x for x in self.board.pieces.values()]

    def move_checker(self, x, y, kill):
        for target in self.board.pieces.values():
            if target.name == kill:
                del self.board.pieces[(target.x, target.y)]
                break

        for checker in self.board.pieces.values():
            if checker.name == self.name:
                print("Found @ ({}, {}) -> ({}, {})".format(checker.x, checker.y, x, y))
                self.board.pieces[(x, y)] = checker
                del self.board.pieces[(checker.x, checker.y)]
                checker.set_pos(x, y)
                if self.turn == "black":
                    self.turn = "red"
                else:
                    self.turn = "black"
                self.valid_moves = []
                self.name = -1
                self.hitlist = []
                break

        for checker in self.board.pieces.values():
            checker.is_king()

    def move_ai(self):
        ai_checkers = []
        for checker in self.board.pieces.values():
            ai_checkers.append((checker.x, checker.y, True if checker.color == "black" else False))

        name, vector = self.move_strats[self.strat].get_move(ai_checkers)

         
