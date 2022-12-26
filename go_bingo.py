from bingo_game import Bingo

class Game:
    def __init__(self):
        pass




if __name__ == '__main__':
    bingo = Bingo()
    playing = True
    while playing:
        print('add the number')
        try:
            number = int(input())
            bingo.add_number(number)
            print('1 for checking a number\n'
                  '2 for checking numbers remaining\n'
                  '3 to check numbers called\n'
                  '4 to create a new game \n'
                  '0 to continue')
            decision = int(input())
            if decision == 1:
                checking = True
                while checking:
                    print('what number do you want to check? ')
                    check_numb = int(input())
                    print(bingo.check_number(check_numb))
                    print('check another number? type "y" or "Y" to continue')
                    again = input()
                    if again in ['y', 'Y']:
                        continue
                    else:
                        checking = False

            elif decision == 2:
                print(bingo.check_current_game())

            elif decision == 3:
                print(bingo.check_current_game())
            else:
                continue

        except TypeError:
            print('please enter a number')
