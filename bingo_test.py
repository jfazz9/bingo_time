import unittest
from bingo_game import Bingo


class TestBingo(unittest.TestCase):
    def test_add_number(self):
        bingo.add_number(9)
        self.assertEqual(bingo.bingo_numbers[0], 9)

    def test_check_number(self):
        bingo.add_number(9)
        self.assertEqual(bingo.check_number(9), True)
        self.assertEqual(bingo.check_number(9), )

    def test_adding


if __name__ == '__main__':
    bingo = Bingo()
    unittest.main()
