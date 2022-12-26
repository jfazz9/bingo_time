class Bingo:
    def __init__(self):
        self.all_numbers = [a for a in range(1,50)]
        self.bingo_numbers = []

    def add_number(self, number):
        try:
            if number in self.all_numbers:
                self.all_numbers.remove(number)
                self.bingo_numbers.append(number)
            else:
                print(f'{number} has already been chosen')

        except ValueError:
            print(f'{number} not in the list try again')

        return self.bingo_numbers

    def check_current_game(self):
        return  print(f'Bingo numbers: {self.bingo_numbers} \n'
                f'remaining numbers {self.all_numbers}')

    def check_number(self, number):
        return number in self.bingo_numbers

    def new_game(self):
        self.all_numbers = [a for a in range(1,50)]
        self.bingo_numbers = []
