# Guess my number game

import random
import datetime

# print a welcome message

print('------------------------------------------------')
print('      WELCOME TO GUESS MY NUMBER GAME           ')
print('------------------------------------------------')
print('The computer chooses a number between 1 and 100 ')
print('You need to guess the number. Maximum trials 10 ')


# Generate a random number
cnum = random.randint(1, 100)
print('[DEBUG]', cnum)

# Create a gaming loop

t1 = datetime.datetime.now()
trials = 1
while trials <= 10:
    unum = int(input('Your Guess >>> '))
    if(unum == cnum):
        print('CONGRATULATIONS!!')
        print('You guessed it right!')
        break
    elif(unum > cnum):
        print('GUESS LOWER...')
        trials += 1
    else:
        print('GUESS HIGHER...')
        trials += 1

t2 = datetime.datetime.now()

# Print results
print('TRIALS: ', trials)
print('TIME TAKEN', t2 - t1)

if(trials <= 3):
    print('Excellent playing')
elif(3 < trials <= 7):
    print('Good playing')
else:
    print('Better luck next time')

print('\n\nThank you!')
    


