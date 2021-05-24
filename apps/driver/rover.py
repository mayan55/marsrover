directions = ['N', 'E', 'S', 'W']


class Rover(object):
    def __init__(self, rover_id, plateau, start_position):
        self.plateau = plateau
        self.position = start_position
        self.last_direction = start_position.direction
        self.rover_id = rover_id
        self.traces = []

    @property
    def active_position(self):
        return '{},{} - {}'.format(self.position.x, self.position.y, self.last_direction)

    @property
    def direction_index(self):
        return directions.index(self.last_direction)

    def point_save(self, direction):
        self.traces.append({direction: self.active_position})

    def run(self, direction):
        if direction == "L":
            self.left()
        elif direction == "R":
            self.right()
        elif direction == "M":
            self.move()

    def left(self):
        self.last_direction = "W" if self.last_direction == "N" else directions[self.direction_index - 1]

    def right(self):
        self.last_direction = "N" if self.last_direction == "W" else directions[self.direction_index + 1]

    def move(self):
        if not self.plateau.line_accessible(self.position):
            print("[Rover]move: point:({},{}), Invalid Coordinate!.".format(self.position.x, self.position.y))
            return
        if self.last_direction == "N":
            self.position.y += 1
        elif self.last_direction == "S":
            self.position.y -= 1
        elif self.last_direction == "E":
            self.position.x += 1
        elif self.last_direction == "W":
            self.position.x -= 1

    def start(self, commands):
        print("[Rover]start: {} --> {}".format(self.rover_id, commands))
        for obj in commands:
            self.run(obj)
            self.point_save(obj)
