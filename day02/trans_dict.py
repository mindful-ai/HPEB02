Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> D = {'name' : 'vijay', 'age': 35, 'country': 'India' }
>>> type(D)
<class 'dict'>
>>> D
{'name': 'vijay', 'age': 35, 'country': 'India'}
>>> D['name']
'vijay'
>>> D['age']
35
>>> D['work']
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    D['work']
KeyError: 'work'
>>> D['work'] = 'student'
>>> D
{'name': 'vijay', 'age': 35, 'country': 'India', 'work': 'student'}
>>> D['work']
'student'
>>> D.setdefault('college')
>>> D
{'name': 'vijay', 'age': 35, 'country': 'India', 'work': 'student', 'college': None}
>>> D.setdefault('salary', '499999')
'499999'
>>> D
{'name': 'vijay', 'age': 35, 'country': 'India', 'work': 'student', 'college': None, 'salary': '499999'}
>>> 'work' in D
True
>>> # del D['key']
>>> D1 = {'native' : 'Bangalore', 'hobby':'guitarist'}
>>> D.update(D1)
>>> D
{'name': 'vijay', 'age': 35, 'country': 'India', 'work': 'student', 'college': None, 'salary': '499999', 'native': 'Bangalore', 'hobby': 'guitarist'}
>>> D.remove('salary')
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    D.remove('salary')
AttributeError: 'dict' object has no attribute 'remove'
>>> D.pop('salary')
'499999'
>>> D
{'name': 'vijay', 'age': 35, 'country': 'India', 'work': 'student', 'college': None, 'native': 'Bangalore', 'hobby': 'guitarist'}
>>> ############################################################
>>> D.keys()
dict_keys(['name', 'age', 'country', 'work', 'college', 'native', 'hobby'])
>>> D.values()
dict_values(['vijay', 35, 'India', 'student', None, 'Bangalore', 'guitarist'])
>>> D.items()
dict_items([('name', 'vijay'), ('age', 35), ('country', 'India'), ('work', 'student'), ('college', None), ('native', 'Bangalore'), ('hobby', 'guitarist')])
>>> D['name']
'vijay'
>>> D['name'] = 'Vijay Kumar'
>>> D
{'name': 'Vijay Kumar', 'age': 35, 'country': 'India', 'work': 'student', 'college': None, 'native': 'Bangalore', 'hobby': 'guitarist'}
>>> person = {'name':'Puneeth', 'age': 35, 'hobbies' : ['guitarist', 'tennis', 'cook'], 'profession': {'company':'HP', 'CEO':'Anthony', 'Place': 'Bangalore', 'Salary':'1599999'} }
>>> person['profession']['CEO']
'Anthony'
>>> 
