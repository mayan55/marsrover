from apps.mars.plateau import Plateau
from apps.utils.position import Position
from apps.driver.rover import Rover


def start_driver(plateau, position, rover_id, commands):
    rover = Rover(rover_id, plateau, position)
    rover.start(commands)
    return rover


plateau = Plateau(5, 5)


def main():
    position = Position(1, 2, 'N')
    res = start_driver(plateau, position, "ROVER_1", "LMLMLMLMM")

    print(res.traces)
    print(res.active_position)

    position = Position(3, 3, 'E')
    res = start_driver(plateau, position, "ROVER_2", "MMRMMRMRRM")

    print(res.traces)
    print(res.active_position)


if __name__ == "__main__":
    main()
