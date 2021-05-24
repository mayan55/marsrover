class Plateau(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.start_x = 0
        self.start_y = 0

    def line_accessible(self, position):
        return self.start_x <= position.x <= self.x and self.start_y <= position.y <= self.y