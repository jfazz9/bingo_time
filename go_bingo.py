from bingo_game import Bingo

class Game:
    def __init__(self):
        pass




if __name__ == '__main__':
    bingo = Bingo()
    print(bingo.all_numbers)
    bingo.add_number(2)
    bingo.add_number(9)
    bingo.check_current_game()
    print(bingo.check_number(9))
    print(bingo.check_number(21))
