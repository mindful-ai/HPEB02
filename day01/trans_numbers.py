Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Numbers
>>> a = 10
>>> b = 20
>>> type(a)
<class 'int'>
>>> c = 22/7
>>> type(c)
<class 'float'>
>>> c
3.142857142857143
>>> # Operators
>>> a + b
30
>>> a - b
-10
>>> a * b
200
>>> a / b
0.5
>>> a ** 3
1000
>>> a > b
False
>>> a < b
True
>>> a >= 10
True
>>> a <= 20
True
>>> a != b
True
>>> a == b/2
True
>>> # in-built functions
>>> a = 100
>>> int(a)
100
>>> bin(a)
'0b1100100'
>>> hex(a)
'0x64'
>>> oct(a)
'0o144'
>>> s = '1001'
>>> type(s)
<class 'str'>
>>> int(s)
1001
>>> int(s, 2)
9
>>> s = '14'
>>> s + 5
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    s + 5
TypeError: can only concatenate str (not "int") to str
>>> int(s) + 5
19
>>> f = 10.445
>>> type(f)
<class 'float'>
>>> int(f) + 4
14
>>> s = '14.56'
>>> int(s) + 5
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    int(s) + 5
ValueError: invalid literal for int() with base 10: '14.56'
>>> float(s) + 5
19.560000000000002
>>> s
'14.56'
>>> abs(float(s) + 5)
19.560000000000002
>>> # Modules
>>> 
>>> factorial(5)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    factorial(5)
NameError: name 'factorial' is not defined
>>> import math
>>> math.factorial(5)
120
>>> math.sqrt(144)
12.0
>>> math.sin(90)
0.8939966636005579
>>> math.sin(90 * (3.14/180))
0.9999996829318346
>>> math.sin(90 * ((22/7)/180))
0.9999998001333682
>>> math.sin(90 * (math.pi / 180))
1.0
>>> math.sin(math.radians(90))
1.0
>>> import random
>>> random.randint(1, 100)
41
>>> random.randint(1, 100)
16
>>> random.randint(1, 100)
22
>>> random.randint(1, 100)
41
>>> random.randint(1, 100)
48
>>> random.randint(1, 100)
20
>>> random.randint(1, 100)
11
>>> random.randint(1, 100)
94
>>> random.randint(1, 100)
39
>>> a = 10
>>> a
10
>>> a = 100
>>> a = 'hello'
>>> a
'hello'
>>> 
