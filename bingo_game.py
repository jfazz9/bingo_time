class Bingo:
    def __init__(self):
        self.all_numbers = [a for a in range(1,50)]
        self.bingo_numbers = []

    def add_number(self, number):
        self.bingo_numbers.append(number)
        self.all_numbers.pop(number)

    def check_current_game(self):
        return f'Bingo numbers: {self.bingo_numbers} \n,
                remaining numbers {self.all_numbers}'

    def check_number(self, number):
        return number in self.bingo_numbers

    def new_game(self):
        self.all_numbers = [a for a in range(1,50)]
        self.bingo_numbers = []
