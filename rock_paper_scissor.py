# rock paper scissor v3

import random


while True:
    def play():
        user = input('Choose one Rock, Paper, Scissor: ').lower()
        computer = random.choice(['rock','paper','scissors'])
        print(f'The computer choose {computer}, And you choose: {user}')

        if user == computer:
            return 'Tie!'
        
        if is_win(user , computer):
            return 'You won'
        
        return 'You lost!'
            
    def is_win(player , enemy):
        if player == 'rock' and enemy == 'scissors' or player == 'paper' and enemy == 'rock' or player == 'scissors' and enemy == 'paper':
            return True

    print(play())
    


