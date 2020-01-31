import random

def jumble(word):
    L = list(word)
    random.shuffle(L)
    jumbledWord = ''.join(L)
    return jumbledWord



###########################################################################


# Read the data

print('Loading game data....')
f = open(r"C:\Users\Purushotham\Desktop\Clients\HPE\HPEB02\day05\words.txt", "r")
content = f.readlines()
f.close()


# Create the dictionary

D = {}
for i in range(1,6):
    D.setdefault(i,content[i-1].strip().split(','))

print('DEBUG',D)


# Banner
print('----------------------------------------------------------- ')
print('      WELCOME TO WORD JUMBLE GAME !!!!                      ')
print('The computer shows you a jumbled word, you are supposed to  ')
print('guess the correct word. You can choose which level you want ')
print('to play.... ')
print('----------------------------------------------------------- ')

# Get the level

level = int(input('Level (1-5): '))

# Load the gaming data

gameData = D[int(level)]

# Start the gaming loop

score = 0
for actWord in gameData:
    jumbledWord = jumble(actWord)
    print(jumbledWord)
    userWord = input('Guess?? ')
    if(userWord == actWord):
        score += 1
        print('You scored a point!!')
    else:
        print('Incorrect guess...')


# Results
print('SCORE :', score)


'''
ASSIGNMENTS:

1. Validate the level
2. Upgrade with more trials (3) for every jumbled word
3. Automatically skip to the next level once the level completes
4. What if you were to add a one clue after the first guess and
   two clues after the second guess?
5. Add 10 entries to each level
'''
