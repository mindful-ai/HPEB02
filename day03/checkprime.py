def checkprime(n):
    for i in range(2, n):
        if(n % i == 0):
            return False
    return True

###################################

if __name__ == '__main__':
    x = int(input('Enter a number: '))
    if(checkprime(x)):
        print('The number is prime')
    else:
        print('The number is not prime')

