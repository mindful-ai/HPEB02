Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s = 'mississippi'
>>> type(s)
<class 'str'>
>>> L = list(s)
>>> L
['m', 'i', 's', 's', 'i', 's', 's', 'i', 'p', 'p', 'i']
>>> T = tuple(s)
>>> T
('m', 'i', 's', 's', 'i', 's', 's', 'i', 'p', 'p', 'i')
>>> S = set(s)
>>> S
{'i', 'm', 's', 'p'}
>>> #################################
>>> s1 = set('abcdef')
>>> s1
{'d', 'f', 'c', 'e', 'b', 'a'}
>>> s2 = {'d', 'e', 'f', 'g', 'h', 'i'}
>>> S1
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    S1
NameError: name 'S1' is not defined
>>> s1
{'d', 'f', 'c', 'e', 'b', 'a'}
>>> s2
{'d', 'i', 'f', 'e', 'g', 'h'}
>>> s1 | s2
{'d', 'i', 'f', 'c', 'e', 'g', 'h', 'b', 'a'}
>>> s1 & s2
{'d', 'e', 'f'}
>>> s1 ^ s2
{'i', 'c', 'g', 'h', 'b', 'a'}
>>> s3 = {'x', 'y', 'z'}
>>> s1
{'d', 'f', 'c', 'e', 'b', 'a'}
>>> s1.add('m')
>>> s1
{'d', 'm', 'f', 'c', 'e', 'b', 'a'}
>>> s1.update(s3)
>>> s1
{'d', 'm', 'z', 'y', 'f', 'c', 'e', 'b', 'a', 'x'}
>>> s1.remove('m')
>>> s1
{'d', 'z', 'y', 'f', 'c', 'e', 'b', 'a', 'x'}
>>> s1.remove('p')
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    s1.remove('p')
KeyError: 'p'
>>> 'p' in s1
False
>>> 'a' in 'apple'
True
>>> s1.intersection(s2)
{'d', 'e', 'f'}
>>> s1.union(s2)
{'d', 'i', 'z', 'y', 'f', 'c', 'e', 'g', 'h', 'b', 'a', 'x'}
>>> s1
{'d', 'z', 'y', 'f', 'c', 'e', 'b', 'a', 'x'}
>>> l1 = sorted(list(s1))
>>> l1
['a', 'b', 'c', 'd', 'e', 'f', 'x', 'y', 'z']
>>> set(l1)
{'d', 'z', 'y', 'f', 'c', 'e', 'b', 'a', 'x'}
>>> 
