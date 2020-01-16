Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> L = list(range(100))
>>> L
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
>>> Ldiv3 = []
>>> for n in L:
	if(n % 3 == 0):
		Ldiv3.append(n)

		
>>> Ldiv3
[0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99]
>>> Ldiv3C = [x for x in L if x % 3 == 0]
>>> Ldiv3C
[0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99]
>>> L = [(x, x**2, x**3) for x in range(10)]
>>> L
[(0, 0, 0), (1, 1, 1), (2, 4, 8), (3, 9, 27), (4, 16, 64), (5, 25, 125), (6, 36, 216), (7, 49, 343), (8, 64, 512), (9, 81, 729)]
>>> text = 'This is a test text for testing python comprehensions
SyntaxError: EOL while scanning string literal
>>> text = 'This is a test text for testing python comprehensions'
>>> D = {x:text.count(x) for x in text}
>>> D
{'T': 1, 'h': 3, 'i': 4, 's': 6, ' ': 8, 'a': 1, 't': 7, 'e': 5, 'x': 1, 'f': 1, 'o': 4, 'r': 2, 'n': 4, 'g': 1, 'p': 2, 'y': 1, 'c': 1, 'm': 1}
>>> L = ['red', 'green', 'blue', 'black', 'grey', 'pink', 'orange']
>>> L1 = [word.upper() for word in L]
>>> L1
['RED', 'GREEN', 'BLUE', 'BLACK', 'GREY', 'PINK', 'ORANGE']
>>> L2 = [(word, len(word)) for word in L if len(word) >= 5]
>>> L2
[('green', 5), ('black', 5), ('orange', 6)]
>>> L
['red', 'green', 'blue', 'black', 'grey', 'pink', 'orange']
>>> L3 = [word.upper() for word in L if 'e' in word]
>>> L3
['RED', 'GREEN', 'BLUE', 'GREY', 'ORANGE']
>>> L4 = [word.upper() if 'e' in word else word for word in L]
>>> L4
['RED', 'GREEN', 'BLUE', 'black', 'GREY', 'pink', 'ORANGE']
>>> 
