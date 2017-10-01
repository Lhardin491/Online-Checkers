from checker import *
import collections

class Board:
    def __init__(self):
        self.pieces = collections.OrderedDict()

    def set_black_pieces(self):
        i = 0
        j = 0
        k = 12
        for i in range(3):
            for j in range(4):
                if i == 0 or i == 2:
                    x = 1+(2*j)
                    y = 7-i
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
                    y = 2-i
                    self.pieces[(x, y)] = (Checker(k, "red", x, y))
                    k += 1
                if i == 1:
                    x = 1+(2*j)
                    y = 2-i
                    self.pieces[(x, y)] = (Checker(k, "red", x, y))
                    k += 1

    def get_valid_moves(self, x, y):
        coordinates = []
        if self.pieces.get((x, y)) is not None:
            if self.pieces[(x, y)].king == True:
                coordinates = [(x+1, y+1), (x+1, y-1), (x+1, y-1),  (x-1, y+1)]
                for i in coordinates:
                    if self.pieces[i] is not None:
                            coordinates.append(
                    if i[0] > 7 or i[1] > 7 or i[0] < 0 or i[1] < 0:
                        coordinates.remove(i)
            else:
                if self.pieces[(x,y)].color == "black":
                    coordinates = [(x-1, y-1), (x+1, y-1)]
                    for i in coordinates:
                         if i[0] > 7 or i[1] > 7 or i[0] < 0 or i[1] < 0:
                            coordinates.remove(i)
                elif self.pieces[(x, y)].color == "red":
                    coordinates = [(x-1, y+1), (x+1, y+1)]
                    for i in coordinates:
                         if i[0] > 7 or i[1] > 7 or i[0] < 0 or i[1] < 0:
                            coordinates.remove(i)
        return coordinates
