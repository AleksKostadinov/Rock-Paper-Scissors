import random
from colorama import Fore

rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'
count_player = 0
count_computer = 0
winner = ''

print(Fore.BLUE + 'This is Rock Paper Scissors Game\nThe game ends when one of the sides reached 5 wins.')
player = input(Fore.WHITE + '\nEnter your name: ')
print(Fore.WHITE + f'Hello, {player}. Good luck!')

while True:
    player_move = input(Fore.LIGHTWHITE_EX + 'Choose [r]ock, [p]aper or [s]cissors: ')

    if player_move == 'r':
        player_move = rock
    elif player_move == 'p':
        player_move = paper
    elif player_move == 's':
        player_move = scissors
    else:
        raise SystemExit('Invalid Input. Try again...')

    computer_random_number = random.randint(1, 3)

    computer_move = ''

    if computer_random_number == 1:
        computer_move = rock
    elif computer_random_number == 2:
        computer_move = paper
    else:
        computer_move = scissors
    print(Fore.WHITE + f'The computer chose {computer_move}.')

    if (player_move == rock and computer_move == scissors) or \
            (player_move == paper and computer_move == rock) or \
            (player_move == scissors and computer_move == paper):
        count_player += 1
        winner = player
        print(Fore.GREEN + 'You win!')
    elif player_move == computer_move:
        print(Fore.YELLOW + 'Draw!')
    else:
        count_computer += 1
        winner = 'Computer'
        print(Fore.RED + 'You lose!')

    print(Fore.WHITE + f'Player: {count_player} Computer: {count_computer}')

    if count_player == 5 or count_computer == 5:
        if winner == player:
            print(Fore.LIGHTGREEN_EX + f'The game ends. The winner is: {winner}')
        else:
            print(Fore.LIGHTRED_EX + f'The game ends. The winner is: {winner}')
        break
