class Checker:
    def __init__(self, color, x, y):
        self.color = color
        self.dead = false
        self.x = x
        self.y = y
        self.king = false

    def kill(self):
        self.dead = true
        
    def set_pos(self, x, y):
        self.x = x
        self.y = y

    def king(self):
        king = true



