import unittest
from bingo_game import Bingo
import random


class TestBingo(unittest.TestCase):
    bingo = Bingo()
    bingo_numb = []
    bingo_id = []

    def test_add_number(self):
        for i in range(1,5):
            number = random.choice(self.bingo.all_numbers)
            self.bingo_numb.append(number)
            total = self.bingo.add_number(number)
            print(total)
            self.assertIsNotNone(total)
            self.bingo_id.append(total)
        print(f'bingo_numb length {len(self.bingo_numb)}')
        print(self.bingo_numb)
        print(f'bingo_id length {len(self.bingo_id)}')
        print(self.bingo_id)

    def test_duplicate(self):
        duplicate = self.bingo_numb[0] #index to one specific number
        old_state = self.bingo_id
        new = self.bingo.add_number(duplicate)
        self.bingo_id.append(new)
        self.assertEqual(old_state[-1], new)
        print('successful duplicate test')
        
    def test_check_number(self):
        self.assertEqual(self.bingo_numb in self.bingo_id, True)

    def test_new_game(self):
        self.bingo.new_game()
        self.assertEqual(self.bingo.bingo_numbers, [])
        self.assertIsNotNone(self.bingo.all_numbers)
        print(self.bingo.all_numbers, self.bingo.bingo_numbers)


if __name__ == '__main__':
    unittest.main()
