# our board class that dows most of the work

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
# generates the valid move options to be used by the gamestate class
    def get_valid_moves(self, x, y):
        coordinates = []
        coordinates2 = []
        movement_vectors = []
        hitlist = []
        hitlist2 = []
        checker = self.pieces.get((x, y))
        if checker is None:
            empty = []
            return empty
        if checker.color == "black":
            movement_vectors.append((-1,-1))
            movement_vectors.append((1,-1))
            if checker.king:
                movement_vectors.append((-1, 1))
                movement_vectors.append((1,1))
        if checker.color == "red":
            movement_vectors.append((-1, 1))
            movement_vectors.append((1, 1))
            if checker.king:
                movement_vectors.append((1, -1))
                movement_vectors.append((-1, -1))
        for i in movement_vectors:
            t = (x+i[0], y+i[1])
            if self.pieces.get(t) is not None and self.pieces.get(t).color != self.pieces.get((x, y)).color:
                t2 = (x+i[0]+i[0], y+i[1]+i[1])
                if self.pieces.get(t2) is None:
                    coordinates.append(t2)
                    hitlist.append(self.pieces.get(t).name)
            elif self.pieces.get(t) is None:
                coordinates.append(t)
                hitlist.append(-1)
        for i, n in zip(coordinates, range(len(coordinates))):
            if i[0] > 7 or i[1] > 7 or i[0] < 0 or i[1] < 0:
                pass
            else:
                coordinates2.append(i)
                hitlist2.append(hitlist[n])
        return (coordinates2, hitlist2)
