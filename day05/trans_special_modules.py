Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> L = ['red', 'red', 'green', 'yellow', 'red', 'green']
>>> from collections import Counter
>>> z = Counter(L)
>>> z
Counter({'red': 3, 'green': 2, 'yellow': 1})
>>> #################################################
>>> from functools import reduce
>>> def formula(a, b):
	return a + b

>>> L = [1,2,3,4,5]
>>> reduce(formula, L)
15
>>> ###################################################
>>> from itertools import permutations, combinations
>>> data = 'ABCD'
>>> permutations(data, 3)
<itertools.permutations object at 0x000002694F9DD830>
>>> list(permutations(data, 3))
[('A', 'B', 'C'), ('A', 'B', 'D'), ('A', 'C', 'B'), ('A', 'C', 'D'), ('A', 'D', 'B'), ('A', 'D', 'C'), ('B', 'A', 'C'), ('B', 'A', 'D'), ('B', 'C', 'A'), ('B', 'C', 'D'), ('B', 'D', 'A'), ('B', 'D', 'C'), ('C', 'A', 'B'), ('C', 'A', 'D'), ('C', 'B', 'A'), ('C', 'B', 'D'), ('C', 'D', 'A'), ('C', 'D', 'B'), ('D', 'A', 'B'), ('D', 'A', 'C'), ('D', 'B', 'A'), ('D', 'B', 'C'), ('D', 'C', 'A'), ('D', 'C', 'B')]
>>> list(combinations(data, 3))
[('A', 'B', 'C'), ('A', 'B', 'D'), ('A', 'C', 'D'), ('B', 'C', 'D')]
>>> ####################################################
>>> from datetime import datetime
>>> t = datetime.now()
>>> t
datetime.datetime(2020, 1, 17, 18, 8, 54, 322173)
>>> t.hour
18
>>> t.second
54
>>> t.year
2020
>>> t.day
17
>>> t.month
1
>>> f = "%A, %d-%B-%y %H:%M:%S"
>>> t.strftime(f)
'Friday, 17-January-20 18:08:54'
>>> f = "%w, %d-%B-%y %H:%M:%S"
>>> t.strftime(f)
'5, 17-January-20 18:08:54'
>>> # https://docs.python.org/3/library/datetime.html
>>> 
>>> ###########################################################
>>> 
>>> from operator import itemgetter
>>> itemgetter(1)('apples')
'p'
>>> itemgetter(1)(['red', 'green', 'blue'])
'green'
>>> f = itemgetter(-1)
>>> type(f)
<class 'operator.itemgetter'>
>>> f('apples')
's'
>>> T = ((x,x**2) for x in range(1, 6))
>>> T
<generator object <genexpr> at 0x000002694F9D4B10>
>>> f(T)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    f(T)
TypeError: 'generator' object is not subscriptable
>>> f(list(T))
(5, 25)
>>> L = ['zebra', 'goat', 'cab', 'max', 'bill']
>>> L.sort()
>>> L
['bill', 'cab', 'goat', 'max', 'zebra']
>>> L.sort(key=f)
>>> L
['zebra', 'cab', 'bill', 'goat', 'max']
>>> ####################################################
>>> 
>>> f = lambda x,y : x + y
>>> f(10, 20)
30
>>> f('abc', 'def')
'abcdef'
>>> f([1,2,3], [3,4,5])
[1, 2, 3, 3, 4, 5]
>>> T = [12, 43, 67, 100]
>>> F = map(lambda t : t * 1.8 + 32, T)
>>> F
<map object at 0x000002694FA01160>
>>> list(F)
[53.6, 109.4, 152.60000000000002, 212.0]
>>> L
['zebra', 'cab', 'bill', 'goat', 'max']
>>> L = ['Zebra', 'cab', 'bill', 'goat', 'Max']
>>> L.sort()
>>> L
['Max', 'Zebra', 'bill', 'cab', 'goat']
>>> L.sort(key = lambda s : s.lower())
>>> L
['bill', 'cab', 'goat', 'Max', 'Zebra']
>>> 
