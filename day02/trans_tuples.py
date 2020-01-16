Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> L = ['red', 'green', 'blue', 'black', 'grey', 'yellow', 'white', 'orange', 'pink']
>>> type(L)
<class 'list'>
>>> T = tuple(L)
>>> T
('red', 'green', 'blue', 'black', 'grey', 'yellow', 'white', 'orange', 'pink')
>>> T[0]
'red'
>>> T[-1]
'pink'
>>> T[::2]
('red', 'blue', 'grey', 'white', 'pink')
>>> T
('red', 'green', 'blue', 'black', 'grey', 'yellow', 'white', 'orange', 'pink')
>>> T = ('red', 'green', 'blue')
>>> T + T
('red', 'green', 'blue', 'red', 'green', 'blue')
>>> T * 3
('red', 'green', 'blue', 'red', 'green', 'blue', 'red', 'green', 'blue')
>>> 'red' in T
True
>>> len(T + T + T)
9
>>> del T[0]
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    del T[0]
TypeError: 'tuple' object doesn't support item deletion
>>> T[0]
'red'
>>> T[-1]
'blue'
>>> T[::]
('red', 'green', 'blue')
>>> T[::-1]
('blue', 'green', 'red')
>>> T
('red', 'green', 'blue')
>>> T.index('red')
0
>>> T.count('black')
0
>>> T.append('blacl')
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    T.append('blacl')
AttributeError: 'tuple' object has no attribute 'append'
>>> sorted(T)
['blue', 'green', 'red']
>>> reversed(T)
<reversed object at 0x000002C6C8313208>
>>> T.sort()
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    T.sort()
AttributeError: 'tuple' object has no attribute 'sort'
>>> T.reverse()
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    T.reverse()
AttributeError: 'tuple' object has no attribute 'reverse'
>>> r,g,b = T
>>> r
'red'
>>> g
'green'
>>> b
'blue'
>>> T
('red', 'green', 'blue')
>>> 
