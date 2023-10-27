states = ('alabama','alaska','arizona','arkansas','california','colorado',
          'connecticut','delaware','florida','georgia','hawaii','idaho',
          'illinois','indiana','iowa','kansas','kentucky','louisiana',
          'maine','maryland','massachusetts','michigan','minnesota',
          'mississippi','missouri','montana','nebraska','nevada',
          'new hampshire','new jersey','new mexico','new york',
          'north carolina','north dakota','ohio','oklahoma','oregon',
          'pennsylvania','rhode island','south carolina','south dakota',
          'tennessee','texas','utah','vermont','virginia','washington'
          ,'west virginia','wisconsin','wyoming')

already_guessed = ('')

from time import *
import os
import sys
game_active = True
progress = ''


while game_active:
    progress_percent = 0
    states_guessed = 0
    sleep(1)
    print('Name all 50 states!')
    sleep(1)
    print('By Malcolm White')
    sleep(1)
    game_started = True
    while game_started:
        print(progress)
        print(f'{progress_percent}% Done')
        state_to_check = str(input('Enter a state: '))
        state_to_check = state_to_check.lower()
        if state_to_check not in states:
            print('Invalid state, try again.')
        elif state_to_check in already_guessed:
            print('You have already guessed that state.')
        elif state_to_check in states:
            already_guessed += state_to_check
            progress += '█' 
            states_guessed += 1
            progress_percent += 2
            print('Correct!')
            sleep(0.5)
            print(f"You've guessed {states_guessed}/50 states.")
            sleep(0.5)
            os.system('cls' if os.name == 'nt' else 'clear')
        elif states_guessed == 50:
            print('You win!')
            game_active == False

            



    
