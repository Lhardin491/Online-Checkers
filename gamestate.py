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
        valid_moves = []
        move = None
        kill = None
        name, vector = self.move_strats[self.strat].get_move(ai_checkers)
        done = False
        while not done:
            for checker in self.board.pieces.values():
                if name == checker.name:
                    valid_moves, hitlist = get_valid_moves(checker.x, checker.y)
                    if vector > len(valid_moves) and len(valid_moves) > 0:
                        move = valid_moves[vector // 2]
                        kill = hitlist[vector // 2]
                        done = True
                    elif len(valid_moves) == 4:
                        move = valid_moves[vector]
                        kill = hitlist[vector]
                        done = True
                    else:
                        name = name + 1 % 12
                        break
       self.name = name
       self.move_checker(move[0], move[1], kill)


