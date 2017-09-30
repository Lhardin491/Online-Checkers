from checker import *
import itertools

class Board:
    def __init__(self):
        self.pieces = {}

    def set_black_pieces(self):
        i = 0
        j = 0
        k = 12
        for i in range(3):
            for j in range(4):
                if i == 0 or i == 2:
                    x = 1+(j*2)
                    y = i
                    self.pieces[(x, y)] = (Checker(k, "black", x, y))
                    k += 1
                if i == 1:
                    x = (2*j)
                    y = (7-i)
                    self.pieces[(x, y)] = (Checker(k, "black", x, y))
                    k += 1
        
    def  set_red_pieces(self):
        i = 0
        j = 0
        k = 0
        for i in range(3):
            for j in range(4):
                if i == 0 or i == 2:
                    x = (2*j)
                    y = 5+i
                    self.pieces[(x, y)] = (Checker(k, "red", x, y))
                    k += 1
                if i == 1:
                    x = 1+(2*j)
                    Y = 5+i
                    self.pieces[(x, y)] = (Checker(k, "red", x, y))
                    k += 1

