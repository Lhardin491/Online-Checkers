from checker import *

class Board:
    def __init__(self):
        self.pieces = []

    def set_black_pieces(self):
        i = 0
        j = 0
        k = 0
        for i in range(3):
            for j in range(4):
                if i == 0 or i == 2:
                    self.pieces.append(Checker(k, "black", 1+(2*j), 7-i))
                    k += 1
                if i == 1:
                    self.pieces.append(Checker(k, "black", (2*j), 7-i))
                    k += 1

        
    def  set_red_pieces(self):
        i = 0
        j = 0
        k = 0
        for i in range(3):
            for j in range(4):
                if i == 0 or i == 2:
                    self.pieces.append(Checker(k, "red", 0+(2*j), 2-i))
                    k += 1
                if i == 1:
                    self.pieces.append(Checker(k, "red", 1+(2*j), 2-i))
                    k += 1

