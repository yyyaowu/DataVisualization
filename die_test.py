import unittest

from Dice.die import Die


class MyTestCase(unittest.TestCase):
    def test_num_side(self):
        die = Die(10)
        self.assertEqual(10, die.num_sides)


if __name__ == "__main__":
    unittest.main()
