import unittest

from apps.driver.rover import Rover
from apps.mars.plateau import Plateau
from apps.utils.position import Position


class TestPlateau(unittest.TestCase):
    def testConstructor(self):
        plateau = Plateau(7, 10)
        # Value Testing
        self.assertEqual(plateau.x, 7)
        self.assertEqual(plateau.y, 10)

        # Line check function testing
        position = Position(1, 11)
        self.assertFalse(plateau.line_accessible(position))

        position = Position(8, 9)
        self.assertFalse(plateau.line_accessible(position))


class TestPositions(unittest.TestCase):
    def testConstructor(self):
        # Default value testing
        position = Position()
        self.assertEqual(position.x, 0)
        self.assertEqual(position.y, 0)
        self.assertEqual(position.direction, 'N')

        # Value testing
        position = Position(1, 2, 'E')
        self.assertEqual(position.x, 1)
        self.assertEqual(position.y, 2)
        self.assertEqual(position.direction, 'E')


class TestRover(unittest.TestCase):
    def testConstructor(self):
        plateau = Plateau(7, 7)
        position = Position(1, 2, "N")

        rover = Rover('ROVER_1', plateau, position)
        self.assertEqual(position, rover.position)
        self.assertEqual(plateau, rover.plateau)

        # Scenario Test 1 (1,2 N) Expected:(1,3 N)
        rover = Rover('ROVER_1', plateau, Position(1, 2, "N"))
        rover.start("LMLMLMLMM")
        self.assertEqual(rover.position, Position(1, 3, "N"))

        # Scenario Test 2 (3,3 E) Expected:(5,1 E)
        rover = Rover('ROVER_2', plateau, Position(3, 3, "E"))
        rover.start("MMRMMRMRRM")
        self.assertEqual(rover.position, Position(5, 1, "E"))

        # Not Expected
        self.assertNotEqual(rover.position, Position(5, 2, "E"))

        # Invalid Coordinate Testing
        rover = Rover('ROVER_2', plateau, Position(3, 3, "E"))
        rover.start("MMRMMRMRRMMMMMM")
        self.assertNotEqual(rover.position, Position(5, 1, "E"))


if __name__ == '__main__':
    unittest.main()
