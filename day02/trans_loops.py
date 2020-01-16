Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> range(10)
range(0, 10)
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(20, 50))
[20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
>>> list(range(1, 100, 5))
[1, 6, 11, 16, 21, 26, 31, 36, 41, 46, 51, 56, 61, 66, 71, 76, 81, 86, 91, 96]
>>> for i in range(10):
	print('Hello HPE')

	
Hello HPE
Hello HPE
Hello HPE
Hello HPE
Hello HPE
Hello HPE
Hello HPE
Hello HPE
Hello HPE
Hello HPE
>>> for i in range(10):
	print('Hello HPE', i)

	
Hello HPE 0
Hello HPE 1
Hello HPE 2
Hello HPE 3
Hello HPE 4
Hello HPE 5
Hello HPE 6
Hello HPE 7
Hello HPE 8
Hello HPE 9
>>> for i in 'abcdef':
	print('Hello ', i)

	
Hello  a
Hello  b
Hello  c
Hello  d
Hello  e
Hello  f
>>> for i in ['red', 'green', 'blue']:
	print('Hello ', i)

	
Hello  red
Hello  green
Hello  blue
>>> s = 'Mary had a little lamb'
>>> for i in s.split():
	print(i, len(i))

	
Mary 4
had 3
a 1
little 6
lamb 4
>>> name = ''
>>> while name != 'quit':
	name = input('Enter name: ')
	print(name.upper())

	
Enter name: Rajesh
RAJESH
Enter name: Ramesh
RAMESH
Enter name: Ritu
RITU
Enter name: Magesh
MAGESH
Enter name: quit
QUIT
>>> names = []
>>> name = ''
>>> while name != 'quit':
	name = input('Enter a name:' )
	names.append(name)

	
Enter a name:Ramesh
Enter a name:Rajesh
Enter a name:Ritu
Enter a name:Magesh
Enter a name:Suresh
Enter a name:Sandeep
Enter a name:quit
>>> names
['Ramesh', 'Rajesh', 'Ritu', 'Magesh', 'Suresh', 'Sandeep', 'quit']
>>> names.pop()
'quit'
>>> name
'quit'
>>> names
['Ramesh', 'Rajesh', 'Ritu', 'Magesh', 'Suresh', 'Sandeep']
>>> import random
>>> rnums = []
>>> for i in range(100):
	rnums.append(random.randint(1, 100))

	
>>> rnums
[85, 2, 46, 74, 60, 18, 32, 79, 35, 53, 52, 10, 83, 71, 44, 13, 43, 66, 41, 21, 26, 81, 41, 72, 25, 63, 16, 45, 69, 76, 4, 64, 16, 16, 70, 89, 57, 70, 49, 37, 95, 48, 42, 35, 75, 51, 15, 84, 35, 4, 41, 69, 56, 97, 51, 38, 1, 29, 30, 1, 46, 30, 46, 36, 28, 30, 62, 92, 51, 70, 58, 91, 83, 6, 54, 65, 79, 7, 43, 81, 77, 42, 41, 76, 19, 26, 19, 5, 41, 81, 10, 6, 9, 46, 100, 66, 29, 2, 74, 67]
>>> temp = set(rnums)
>>> temp
{1, 2, 4, 5, 6, 7, 9, 10, 13, 15, 16, 18, 19, 21, 25, 26, 28, 29, 30, 32, 35, 36, 37, 38, 41, 42, 43, 44, 45, 46, 48, 49, 51, 52, 53, 54, 56, 57, 58, 60, 62, 63, 64, 65, 66, 67, 69, 70, 71, 72, 74, 75, 76, 77, 79, 81, 83, 84, 85, 89, 91, 92, 95, 97, 100}
>>> urnums = list(temp)
>>> urnums
[1, 2, 4, 5, 6, 7, 9, 10, 13, 15, 16, 18, 19, 21, 25, 26, 28, 29, 30, 32, 35, 36, 37, 38, 41, 42, 43, 44, 45, 46, 48, 49, 51, 52, 53, 54, 56, 57, 58, 60, 62, 63, 64, 65, 66, 67, 69, 70, 71, 72, 74, 75, 76, 77, 79, 81, 83, 84, 85, 89, 91, 92, 95, 97, 100]
>>> len(rnums)
100
>>> len(urnums)
65
>>> odds = []
>>> evens = []
>>> for num in urnums:
	if( num % 2 == 0 ):
		evens.append(num)
	else:
		odds.append(num)

		
>>> odds
[1, 5, 7, 9, 13, 15, 19, 21, 25, 29, 35, 37, 41, 43, 45, 49, 51, 53, 57, 63, 65, 67, 69, 71, 75, 77, 79, 81, 83, 85, 89, 91, 95, 97]
>>> evens
[2, 4, 6, 10, 16, 18, 26, 28, 30, 32, 36, 38, 42, 44, 46, 48, 52, 54, 56, 58, 60, 62, 64, 66, 70, 72, 74, 76, 84, 92, 100]
>>> print(5 + ' X ' + 1 + ' = ' + (5 * 1))
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    print(5 + ' X ' + 1 + ' = ' + (5 * 1))
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> print(str(5) + ' X ' + str(1) + ' = ' + str(5 * 1))
5 X 1 = 5
>>> for i in range(1, 11):
	print(str(5) + ' X ' + str(i) + ' = ' + str(5 * i))

	
5 X 1 = 5
5 X 2 = 10
5 X 3 = 15
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
5 X 8 = 40
5 X 9 = 45
5 X 10 = 50
>>> 
