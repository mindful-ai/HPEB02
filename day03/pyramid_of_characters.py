# Program to print character pyramid

# Inputs

L = int(input('Number of lines:' ))
C = input('Enter the character:')


# Process

smin = L + 10 #(2*L - 1)/2

for line in range(1, L + 1):
    pstr = ' ' * int(smin) + C * (2*line - 1)
    print(pstr)
    smin = smin - 1
