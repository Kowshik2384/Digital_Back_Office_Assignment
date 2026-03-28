import unittest
from plateau import Plateau
from rover import Rover

class TestRover(unittest.TestCase):
    
    def setUp(self):
        self.plateau = Plateau(5, 5)

    def test_sample_case_1(self):
        rover = Rover(1, 2, 'N', self.plateau)
        rover.execute('LMLMLMLMM')
        self.assertEqual(rover.get_position(), '1 3 N')

    def test_sample_case_2(self):
        rover = Rover(3, 3, 'E', self.plateau)
        rover.execute('MMRMMRMRRM')
        self.assertEqual(rover.get_position(), '5 1 E')

    def test_invalid_command(self):
        rover = Rover(1, 2, 'N', self.plateau)
        with self.assertRaises(ValueError):
            rover.execute('LMX')

    def test_boundary_condition(self):
        """Rover should not move past the plateau boundaries."""
        rover = Rover(5, 5, 'N', self.plateau)
        rover.execute('M') # tries to move to (5, 6)
        # Should stay at 5 5 N because moving out of bounds is ignored
        self.assertEqual(rover.get_position(), '5 5 N')
        
    def test_left_and_right_turns(self):
        rover = Rover(0, 0, 'N', self.plateau)
        rover.execute('L')
        self.assertEqual(rover.get_position(), '0 0 W')
        rover.execute('R')
        self.assertEqual(rover.get_position(), '0 0 N')
        rover.execute('RR')
        self.assertEqual(rover.get_position(), '0 0 S')

if __name__ == '__main__':
    unittest.main()
