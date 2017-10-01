# Our checker class

class Checker:
    def __init__(self, name, color, x, y):
        self.color = color
        self.dead = False
        self.x = x
        self.y = y
        self.king = False
        self.name = name
# defines if the piece is in play or not
    def kill(self):
        self.dead = True
# tracks the position of the piece
    def set_pos(self, x, y):
        self.x = x
        self.y = y
# defines if the piece is 'king' or not
    def is_king(self):
        if self.color == "red" and self.y == 7:
            self.king = True
        elif self.color == "black" and self.y == 0:
            self.king = True
# gives a string value to be printed (for testing)
    def __repr__(self):
        s = "({}, {}) $ {}".format(self.x, self.y, self.name)
        return s

