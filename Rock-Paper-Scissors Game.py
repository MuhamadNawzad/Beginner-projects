import random
command = ''
wins = 0
loses = 0
draws = 0
while True:
    command = input('Choose (r) rock, (p) paper, (s) scissor or (q) to quit: ')
    computer = random.choice(['r', 'p', 's'])
    while command not in ['r', 'p', 's', 'q']:
        command = input('Choose (r) rock, (p) paper, (s) scissor or (q) to quit: ')
    if command == 'q':
        break
    else:
        if computer == 'r':
            move = 'rock'
        elif computer == 'p':
            move = 'paper'
        elif computer == 's':
            move = 'scissor'
        print('computer chooses ' + str(move))
        if (command == 'r' and computer == 's') or (command == 'p' and computer == 'r') or \
                (command == 's' and computer == 'p'):
            wins += 1
        elif computer == command:
            draws += 1
        else:
            loses += 1
print('You have ' + str(wins) + ' Wins, ' + str(draws) + ' Draws and ' + str(loses) + ' Loses.')
