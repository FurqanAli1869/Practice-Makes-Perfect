import random
# RPS = ['ROCK', 'PAPER', 'SCISSORS']
# i = 0
# your_score = 0
# comp_score = 0
print("You'll play 3 games against the computer. A deuce doesnt count as a game. Let's begin!")


def game():
    i = 0
    your_score = 0
    comp_score = 0
    trials = your_score + comp_score
    trials = 0
    while trials:
        person = input('Rock, Paper, or Scissors? (case-sensitive input!)   ')
        computer = random.randint(0, 2)
        while computer == 0:
            computer = 'Rock'
            print(f'The computer chose {computer}')
            i += 1
            if person == 'Rock':
                i = 0
                print('Deuce! Lets try again')
                game()
            elif person == 'Paper':
                your_score += 1
            else:
                comp_score += 1

        while computer == 1:
            computer = 'Paper'
            print(f'The computer chose {computer}')
            i += 1
            if person == 'Rock':
                comp_score += 1
            elif person == 'Paper':
                i = 0
                print('Deuce! Lets try again')
                game()
            else:
                your_score += 1

        while computer == 2:
            computer = 'Scissors'
            print(f'The computer chose {computer}')
            i += 1
            if person == 'Rock':
                your_score += 1
            elif person == "Paper":
                comp_score += 1
            else:
                i = 0
                print('Deuce! Lets try again')
                game()

    print(2 * '\n')
    if your_score > comp_score:
        print('You won!')

    elif your_score == comp_score:
        print('You lost!')

    print(f'Your score is {your_score}, and the computer\'s is {comp_score}.')

game()









