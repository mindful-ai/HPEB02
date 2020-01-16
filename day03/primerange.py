
import checkprime
start = int(input('Enter the start of the range: '))
end = int(input('Enter end of the range: '))

primes = [n for n in range(start, end+1) if checkprime.checkprime(n)]
print('PRIMES: \n', primes)

