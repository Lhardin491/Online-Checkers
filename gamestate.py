from board import *
from genetics import *
import random
import itertools
import collections

class GameState:
    def __init__(self):
        self.num_strats = 3
        self.mutate_chance = 0.01
        self.board = Board()
        self.board.set_red_pieces()
        self.board.set_black_pieces()
        self.valid_moves = []
        self.hitlist = []
        self.name = -1
        self.turn = "black"
        self.move_strats = [MovementStrategy()] * self.num_strats
        self.strat = -1
        self.generation =0
        print("------- Generation {} --------".format(self.generation))

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
        if self.board.pieces.get((x, y)) is not None and self.board.pieces.get((x, y)).color == "black":
            self.name = self.board.pieces.get((x, y)).name
            self.valid_moves, self.hitlist = self.board.get_valid_moves(x, y)
       
    def get_ghosts(self):
        return self.valid_moves

    def get_checkers(self):
        return [x for x in self.board.pieces.values()]

    def move_checker(self, x, y, kill):
        for target in self.board.pieces.values():
            if target.name == kill:
                if self.turn == "black":
                    self.move_strats[self.strat].score -= 1
                else:
                    self.move_strats[self.strat].score += 2
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
        self.strat = (self.strat + 1) % self.num_strats
        ai_checkers = []
        for checker in self.board.pieces.values():
            ai_checkers.append((checker.x, checker.y, True if checker.color == "black" else False))
        valid_moves = []
        move = None
        kill = None
        name, vector = self.move_strats[self.strat].get_move(ai_checkers)
        vector2 = -1
        done = False
        failsafe = 15
        while not done and failsafe > 0:
            print("Looking for {}", name)
            for checker in self.board.pieces.values():
                print(checker)
                if name == checker.name:
                    valid_moves, hitlist = self.board.get_valid_moves(checker.x, checker.y)
                    vector2 = vector
                    if len(valid_moves) > 0:
                        while vector2 >= len(valid_moves):
                            vector2 -= 1
                            print("Vector2 => {}".format(vector2))
                        move = valid_moves[vector2]
                        kill = hitlist[vector2]
                        print("Kill => {}".format(kill))
                        done = True
                    else:
                        name = (name + 1) % 12
                        print("Updated name to {}".format(name))
                        break
            if not done:
                name = (name + 1) % 12
                failsafe -= 1

        if failsafe <= 0:
            self.turn = "black"
            return

        self.name = name
        self.move_checker(move[0], move[1], kill)

    def wined(self):
        black_win = True
        red_win = True
        game_over = False
        for checker in self.board.pieces.values():
            if checker.color == "black":
                black_win = False
            if checker.color == "red":
                red_win = False
        if black_win or red_win:
            game_over = True
        return (game_over, black_win)


    def next_round(self):
        new_pop = []
        breeders = choices(self.move_strats, weights=[x.score for x in self.move_strats], k=self.num_strats * 2)
        print(breeders)
        for breeder1, breeder2 in zip(itertools.islice(breeders, 0, None, 2), itertools.islice(breeders, 1, None, 2)):
            offspring = breeder1.breed(breeder2)
            offspring.mutate(self.mutate_chance)
            self.mutate_chance += 0.005
            new_pop.append(offspring)
        self.move_strats = new_pop
        self.board = Board()
        self.board.set_red_pieces()
        self.board.set_black_pieces()
        self.valid_moves = []
        self.hitlist = []
        self.name = -1
        self.turn = "black"
        self.strat = -1
        self.generation += 1
        print("------- Generation {} --------".format(self.generation))

def choices(seq, weights=None, k=1):
    assert len(weights) == len(seq)
    bias = min(weights)
    if bias <= 0:
        bias = (-bias) + 1
    sample = []
    yep = []
    print("weights={}".format(weights))
    for weight, i in zip(map(lambda q: q + bias, weights), range(len(seq))):
        for m in range(weight):
            print("Adding {}".format(seq[i]))
            sample.append(seq[i])
    
    for h in range(k):
       bb = random.choice(sample) 
       yep.append(bb)

    return yep

