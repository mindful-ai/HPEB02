# Program to count the vowels in the text

# Input

text = input('Enter some text: ')

# Process

text = text.lower()
acnt = text.count('a')
ecnt = text.count('e')
icnt = text.count('i')
ocnt = text.count('o')
ucnt = text.count('u')

vowelCount = acnt + ecnt + icnt + ocnt + ucnt

# Output

print('A/a --> ', acnt)
print('E/e --> ', ecnt)
print('I/i --> ', icnt)
print('O/o --> ', ocnt)
print('U/u --> ', ucnt)
print('----------------------------------')
print('Total vowels in the text: ', vowelCount)
