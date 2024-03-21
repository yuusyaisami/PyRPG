class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Camera:
    def __init__(self, x=0, y=0):
        self.pos = Position(x, y)