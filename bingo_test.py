import unittest
from bingo_game import Bingo
import random


class TestBingo(unittest.TestCase):
    bingo = Bingo()
    bingo_numb = []
    bingo_id = []

    def test_add_number(self):
        for i in range(1,5):
            number = random.choice(bingo.all_numbers)
            self.bingo_numb.append(number)
            total = self.bingo.add_number(number)
            print(total)
            self.assertIsNotNone(total)
            self.bingo_id.append(total)
        print(f'bingo_numb length {len(self.bingo_numb)}')
        print(self.bingo_numb)
        print(f'bingo_id length {len(self.bingo_id)}')
        print(self.bingo_id)


    def test_check_number(self):
        self.assertEqual(self.bingo_numb in self.bingo_id, True)


    # def test_adding(self):
    #     self.assertEqual(2 in bingo.all_numbers, True)
    #     self.assertEqual(9 in bingo.all_numbers, False)
    #     self.assertEqual(9 in bingo.bingo_numbers, True)
    #     self.assertEqual(2 in bingo.bingo_numbers, False)

    # def test_new_game(self):
    #     bingo.new_game()
    #     self.assertEqual()

if __name__ == '__main__':
    unittest.main()
