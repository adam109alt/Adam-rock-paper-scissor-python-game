import random

while True:
    
    gusse = input('Enter your gusse: ').lower()
    
    if gusse == 'rock':
        print(f'You choose {gusse}')
    elif gusse == 'scssior':
        print(f'You choose {gusse}')
    elif gusse == 'paper':
        print(f'you choose {gusse}')
        
    else:
        print('Invalid')
        
    cont = input('If you want to continue type y and if you want to stop type n: ')
    
    if cont == 'y':
        computer_gusses = random.randint(1 , 3)
        if computer_gusses == 1:
            print(f'The computer gusse is: Rock')
        elif computer_gusses == 2:
            print(f'The computer gusse is: Scissor')
        elif computer_gusses == 3:
            print(f'The computer gusse is: Paper')
        
    elif cont == 'n':
        print('BYE!')
        break
    else:
        print('Invalid!')
        
    if computer_gusses == 1 and gusse == 'rock':
        print('Its tie ')
        
    elif computer_gusses == 2 and gusse == 'scssior':
        print('Its tie ')
        
    elif computer_gusses == 3 and gusse == 'paper':
        print('Its tie ')
        
    elif computer_gusses == 1 and gusse == 'scssior':
        print('Computer won')
        
    elif computer_gusses == 2 and gusse == 'rock':
        print('You win')
        
    elif computer_gusses == 3 and gusse == 'scssior':
        print('you win')
        
    elif computer_gusses == 2 and gusse == 'paper':
        print('compuer win')
        
    elif computer_gusses == 3 and gusse == 'rock':
        print('you win')
    elif computer_gusses == 1 and gusse == 'paper':
        print('you win')
