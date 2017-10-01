class Checker:
    def __init__(self, name, color, x, y):
        self.color = color
        self.dead = False
        self.x = x
        self.y = y
        self.king = False
        self.name = name

    def kill(self):
        self.dead = True
        
    def set_pos(self, x, y):
        self.x = x
        self.y = y

    def is_king(self):
        if self.color == "red" and self.y == 7:
            self.king = True
        elif self.color == "black" and self.y == 0:
            self.king = True

    def __repr__(self):
        s = "({}, {}) $ {}".format(self.x, self.y, self.name)
        return s

