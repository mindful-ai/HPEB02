import random

def genpass():

    charclass = ['special', 'upper', 'lower', 'number']
    passlen   = random.randint(8, 17)

    specials  = list('@#$%&*~()_+=')

    passchars = []
    while len(passchars) != passlen:
        # Randomly choose a character class
        choice = random.choice(charclass)

        # Generate a character
        if(choice == 'special'):
            char = random.choice(specials)

        if(choice == 'upper'):
            char = chr(random.randint(65, 91))

        if(choice == 'lower'):
            char = chr(random.randint(97, 123))

        if(choice == 'number'):
            char = str(random.choice(list(range(10))))

        # If the container is empty, add the first character
        if(len(passchars) == 0):
            passchars.append(char)

        # If the container is not empty, check if the last character is
        # same as the currently produced charater
        if(passchars[-1] != char):
            passchars.append(char)
        else:
            pass

    # As an extra care, shuffle the passchars several times

    n = random.randint(1, 100)
    for i in range(n):
        random.shuffle(passchars)

    # Join all the characters to create a password
    password = ''.join(passchars)

    return password
