class Position(object):
    def __init__(self, x=0, y=0, direction="N"):
        self.x = x
        self.y = y
        self.direction = direction

    def __eq__(self, position):
        return self.x == position.x and self.y == position.y