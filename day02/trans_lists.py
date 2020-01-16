Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> L1 = ['apple', 'ball', 4, 5, 6, 1.9, -10, True, False, [1, 2, 3]]
>>> print(L1)
['apple', 'ball', 4, 5, 6, 1.9, -10, True, False, [1, 2, 3]]
>>> L[-1]
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    L[-1]
NameError: name 'L' is not defined
>>> L1[-1]
[1, 2, 3]
>>> L[-1][2]
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    L[-1][2]
NameError: name 'L' is not defined
>>> L1[-1][2]
3
>>> ####################################################
>>> L = ['red', 'green', 'blue']
>>> LG = ['black', 'grey', 'white']
>>> L + LG
['red', 'green', 'blue', 'black', 'grey', 'white']
>>> L3 = L + LG
>>> L3
['red', 'green', 'blue', 'black', 'grey', 'white']
>>> L * 3
['red', 'green', 'blue', 'red', 'green', 'blue', 'red', 'green', 'blue']
>>> 'green' in L
True
>>> 'grey' in L
False
>>> 'grey' in L + LG
True
>>> len(L + LG)
6
>>> L1
['apple', 'ball', 4, 5, 6, 1.9, -10, True, False, [1, 2, 3]]
>>> del L1[4]
>>> L1
['apple', 'ball', 4, 5, 1.9, -10, True, False, [1, 2, 3]]
>>> ######################################################
>>> L
['red', 'green', 'blue']
>>> L[2] = 'yellow'
>>> L
['red', 'green', 'yellow']
>>> L[2]
'yellow'
>>> L[2][1] = 'g'
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    L[2][1] = 'g'
TypeError: 'str' object does not support item assignment
>>> ########################################################
>>> L3
['red', 'green', 'blue', 'black', 'grey', 'white']
>>> L[2]
'yellow'
>>> L[-2]
'green'
>>> L
['red', 'green', 'yellow']
>>> L3
['red', 'green', 'blue', 'black', 'grey', 'white']
>>> L3[-2]
'grey'
>>> L3[1:5]
['green', 'blue', 'black', 'grey']
>>> L3[-4:-1]
['blue', 'black', 'grey']
>>> L3[:]
['red', 'green', 'blue', 'black', 'grey', 'white']
>>> L3[::1]
['red', 'green', 'blue', 'black', 'grey', 'white']
>>> L3[::2]
['red', 'blue', 'grey']
>>> L3[::-1]
['white', 'grey', 'black', 'blue', 'green', 'red']
>>> L3[1:1]
[]
>>> L3[1:2]
['green']
>>> L3
['red', 'green', 'blue', 'black', 'grey', 'white']
>>> L3[:1]
['red']
>>> L[0]
'red'
>>> #####################################################
>>> L
['red', 'green', 'yellow']
>>> L1
['apple', 'ball', 4, 5, 1.9, -10, True, False, [1, 2, 3]]
>>> L2
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    L2
NameError: name 'L2' is not defined
>>> L3
['red', 'green', 'blue', 'black', 'grey', 'white']
>>> L3
['red', 'green', 'blue', 'black', 'grey', 'white']
>>> L3.append('orange')
>>> L3
['red', 'green', 'blue', 'black', 'grey', 'white', 'orange']
>>> L3.append('pink')
>>> L3
['red', 'green', 'blue', 'black', 'grey', 'white', 'orange', 'pink']
>>> L3.insert(-3, 'yellow')
>>> L3
['red', 'green', 'blue', 'black', 'grey', 'yellow', 'white', 'orange', 'pink']
>>> L3.insert(-2. 'cyan')
SyntaxError: invalid syntax
>>> L3.insert(-2, 'cyan')
>>> L3
['red', 'green', 'blue', 'black', 'grey', 'yellow', 'white', 'cyan', 'orange', 'pink']
>>> L4 = ['magenta', 'purple', 'maroon']
>>> L3.append(L4)
>>> L3
['red', 'green', 'blue', 'black', 'grey', 'yellow', 'white', 'cyan', 'orange', 'pink', ['magenta', 'purple', 'maroon']]
>>> L3.pop()
['magenta', 'purple', 'maroon']
>>> L3
['red', 'green', 'blue', 'black', 'grey', 'yellow', 'white', 'cyan', 'orange', 'pink']
>>> L3.extent(L4)
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    L3.extent(L4)
AttributeError: 'list' object has no attribute 'extent'
>>> L3.extend(L4)
>>> L3
['red', 'green', 'blue', 'black', 'grey', 'yellow', 'white', 'cyan', 'orange', 'pink', 'magenta', 'purple', 'maroon']
>>> # Removing elements
>>> L3.pop()
'maroon'
>>> L3
['red', 'green', 'blue', 'black', 'grey', 'yellow', 'white', 'cyan', 'orange', 'pink', 'magenta', 'purple']
>>> L3.pop()
'purple'
>>> L3
['red', 'green', 'blue', 'black', 'grey', 'yellow', 'white', 'cyan', 'orange', 'pink', 'magenta']
>>> L3.pop(2)
'blue'
>>> L3
['red', 'green', 'black', 'grey', 'yellow', 'white', 'cyan', 'orange', 'pink', 'magenta']
>>> L3.insert(2, 'blue')
>>> L3
['red', 'green', 'blue', 'black', 'grey', 'yellow', 'white', 'cyan', 'orange', 'pink', 'magenta']
>>> 'cyan; in L3
SyntaxError: EOL while scanning string literal
>>> 'cyan' in L3
True
>>> L3.remove('cyan')
>>> L3
['red', 'green', 'blue', 'black', 'grey', 'yellow', 'white', 'orange', 'pink', 'magenta']
>>> # Searching
>>> L3.index('grey')
4
>>> L3.count('red')
1
>>> L3.extend(['red', 'red'])
>>> L3
['red', 'green', 'blue', 'black', 'grey', 'yellow', 'white', 'orange', 'pink', 'magenta', 'red', 'red']
>>> L3.count('red')
3
>>> # Rearranging
>>> L = ['apples', 'zebra', 'goat', 'bat', 'sheep']
>>> reversed(L)
<list_reverseiterator object at 0x0000024091530320>
>>> list(reversed(L))
['sheep', 'bat', 'goat', 'zebra', 'apples']
>>> L
['apples', 'zebra', 'goat', 'bat', 'sheep']
>>> LR = list(reversed(L))
>>> LR
['sheep', 'bat', 'goat', 'zebra', 'apples']
>>> L
['apples', 'zebra', 'goat', 'bat', 'sheep']
>>> L.reverse()
>>> L
['sheep', 'bat', 'goat', 'zebra', 'apples']
>>> sorted(L)
['apples', 'bat', 'goat', 'sheep', 'zebra']
>>> L
['sheep', 'bat', 'goat', 'zebra', 'apples']
>>> L.sort()
>>> L
['apples', 'bat', 'goat', 'sheep', 'zebra']
>>> L.sort(reverse=True)
>>> L
['zebra', 'sheep', 'goat', 'bat', 'apples']
>>> ####
>>> L
['zebra', 'sheep', 'goat', 'bat', 'apples']
>>> LC = L
>>> L
['zebra', 'sheep', 'goat', 'bat', 'apples']
>>> LC
['zebra', 'sheep', 'goat', 'bat', 'apples']
>>> L[-2] = 'banana'
>>> L
['zebra', 'sheep', 'goat', 'banana', 'apples']
>>> LC
['zebra', 'sheep', 'goat', 'banana', 'apples']
>>> Lc.append('cat')
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    Lc.append('cat')
NameError: name 'Lc' is not defined
>>> LC.append('cat')
>>> LC
['zebra', 'sheep', 'goat', 'banana', 'apples', 'cat']
>>> L
['zebra', 'sheep', 'goat', 'banana', 'apples', 'cat']
>>> from copy import deepcopy
>>> L
['zebra', 'sheep', 'goat', 'banana', 'apples', 'cat']
>>> LC
['zebra', 'sheep', 'goat', 'banana', 'apples', 'cat']
>>> LD = deepcopy(L)
>>> LD
['zebra', 'sheep', 'goat', 'banana', 'apples', 'cat']
>>> L.append('elephant')
>>> L
['zebra', 'sheep', 'goat', 'banana', 'apples', 'cat', 'elephant']
>>> LC
['zebra', 'sheep', 'goat', 'banana', 'apples', 'cat', 'elephant']
>>> LD
['zebra', 'sheep', 'goat', 'banana', 'apples', 'cat']
>>> del LC
>>> L
['zebra', 'sheep', 'goat', 'banana', 'apples', 'cat', 'elephant']
>>> LC
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    LC
NameError: name 'LC' is not defined
>>> LD
['zebra', 'sheep', 'goat', 'banana', 'apples', 'cat']
>>> L
['zebra', 'sheep', 'goat', 'banana', 'apples', 'cat', 'elephant']
>>> LC = L[1:5]
>>> L
['zebra', 'sheep', 'goat', 'banana', 'apples', 'cat', 'elephant']
>>> LC
['sheep', 'goat', 'banana', 'apples']
>>> L.insert(2, 'tiger')
>>> L
['zebra', 'sheep', 'tiger', 'goat', 'banana', 'apples', 'cat', 'elephant']
>>> LC
['sheep', 'goat', 'banana', 'apples']
>>> 
