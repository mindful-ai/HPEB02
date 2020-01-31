Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:\Users\Purushotham\Desktop\Clients\HPE\HPEB01\Classwork\day04\student.py 
NAME:  Vijay
AGE:  14
REG ID: HPE007
-----------------------------------
MATHS    :  0
PHYSICS  :  0
CHEMISTRY:  0
BIOLOGY  :  0
-----------------------------------
AVERAGE  :  0
RANK     :  0



Incorrect subject code
Incorrect subject code
NAME:  Vijay
AGE:  14
REG ID: HPE007
-----------------------------------
MATHS    :  0
PHYSICS  :  100
CHEMISTRY:  100
BIOLOGY  :  0
-----------------------------------
AVERAGE  :  0
RANK     :  0



NAME:  Hemanth
AGE:  14
REG ID: HPE006
-----------------------------------
MATHS    :  0
PHYSICS  :  0
CHEMISTRY:  0
BIOLOGY  :  0
-----------------------------------
AVERAGE  :  0
RANK     :  0



NAME:  Vijay
AGE:  14
REG ID: HPE007
-----------------------------------
MATHS    :  88
PHYSICS  :  100
CHEMISTRY:  100
BIOLOGY  :  100
-----------------------------------
AVERAGE  :  0
RANK     :  0



Setting rank
NAME:  Vijay
AGE:  14
REG ID: HPE007
-----------------------------------
MATHS    :  88
PHYSICS  :  100
CHEMISTRY:  100
BIOLOGY  :  100
-----------------------------------
AVERAGE  :  97.0
RANK     :  1



>>> 
>>> 
>>> 
>>> 'my name is {} and age is {}'.format('Raj', 24)
'my name is Raj and age is 24'
>>> 'my name is {0} and age is {1}'.format('Raj', 24)
'my name is Raj and age is 24'
>>> 'my name is {1} and age is {0}'.format('Raj', 24)
'my name is 24 and age is Raj'
>>> template = 'my name is {name}, age is {age} and I am from {place}'
>>> template.format('Raj', 23, 'Bangalore')
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    template.format('Raj', 23, 'Bangalore')
KeyError: 'name'
>>> template.format(name='Raj', age=23, place='Bangalore')
'my name is Raj, age is 23 and I am from Bangalore'
>>> template = 'my name is {name:>20}, age is {age:<10} and I am from {place:^15}'
>>> template.format(name='Raj', age=23, place='Bangalore')
'my name is                  Raj, age is 23         and I am from    Bangalore   '
>>> 
