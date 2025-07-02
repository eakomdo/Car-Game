#A car game that allows the user to drive a car and avoid obstacles.

need_help = input('Do you need help on driving? (yes/no) ').lower()

while need_help == 'yes':
    print('Welcome to the car game!')
    print('In this game, you will drive a car and avoid obstacles.')
    
    print('Good luck!')
    if need_help == 'yes':
        print('Here are some tips to help you drive:')
        
        drive = input('Type start to move your car or press enter to continue: ').strip().lower()
        if drive == 'start':
            print('You have started driving.')
            break
       
        
        stop = input('Type stop to stop your car or press enter to continue: ').strip().lower()
        if stop == 'stop':
            print('You have stopped driving.')
            break

        quit_input = input('Type quit to exit the game or press enter to continue: ').strip().lower()
        if quit_input == 'quit':
            print('Thank you for playing!')
            break
        
    else:
        print('Invalid input. Please try again.')
    
    
else:
   print ('Thank you for playing!')