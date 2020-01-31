Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> f = open(r"C:\Users\Purushotham\Desktop\Clients\HPE\HPEB02\day04\hc.txt", "r")
>>> f
<_io.TextIOWrapper name='C:\\Users\\Purushotham\\Desktop\\Clients\\HPE\\HPEB02\\day04\\hc.txt' mode='r' encoding='cp1252'>
>>> type(f)
<class '_io.TextIOWrapper'>
>>> c = f.read()
>>> c
'On a dark desert highway, cool wind in my hair\nWarm smell of colitas, rising up through the air\nUp ahead in the distance, I saw a shimmering light\nMy head grew heavy and my sight grew dim\nI had to stop for the night.\nThere she stood in the doorway;\nI heard the mission bell\nAnd I was thinking to myself\n\'This could be heaven or this could be Hell\'\nThen she lit up a candle and she showed me the way\nThere were voices down the corridor,\nI thought I heard them say\nWelcome to the Hotel California\nSuch a lovely place (such a lovely place)\nSuch a lovely face.\nPlenty of room at the Hotel California\nAny time of year (any time of year) you can find it here\nHer mind is Tiffany-twisted, she got the Mercedes bends\nShe got a lot of pretty, pretty boys, that she calls friends\nHow they dance in the courtyard, sweet summer sweat\nSome dance to remember, some dance to forget\nSo I called up the Captain,\n\'Please bring me my wine\'\nHe said, \'we haven\'t had that spirit here since nineteen sixty-nine\'\nAnd still those voices are calling from far away,\nWake you up in the middle of the night\nJust to hear them say"\nWelcome to the Hotel California\nSuch a lovely place (such a lovely place)\nSuch a lovely face.\nThey livin\' it up at the Hotel California\nWhat a nice surprise (what a nice surprise), bring your alibis\nMirrors on the ceiling,\nThe pink champagne on ice\nAnd she said, \'we are all just prisoners here, of our own device\'\nAnd in the master\'s chambers,\nThey gathered for the feast\nThey stab it with their steely knives,\nBut they just can\'t kill the beast\nLast thing I remember, I was\nRunning for the door\nI had to find the passage back to the place I was before\n\'Relax\' said the night man,\n\'We are programmed to receive.\nYou can check out any time you like,\nBut you can never leave!\''
>>> print(c)
On a dark desert highway, cool wind in my hair
Warm smell of colitas, rising up through the air
Up ahead in the distance, I saw a shimmering light
My head grew heavy and my sight grew dim
I had to stop for the night.
There she stood in the doorway;
I heard the mission bell
And I was thinking to myself
'This could be heaven or this could be Hell'
Then she lit up a candle and she showed me the way
There were voices down the corridor,
I thought I heard them say
Welcome to the Hotel California
Such a lovely place (such a lovely place)
Such a lovely face.
Plenty of room at the Hotel California
Any time of year (any time of year) you can find it here
Her mind is Tiffany-twisted, she got the Mercedes bends
She got a lot of pretty, pretty boys, that she calls friends
How they dance in the courtyard, sweet summer sweat
Some dance to remember, some dance to forget
So I called up the Captain,
'Please bring me my wine'
He said, 'we haven't had that spirit here since nineteen sixty-nine'
And still those voices are calling from far away,
Wake you up in the middle of the night
Just to hear them say"
Welcome to the Hotel California
Such a lovely place (such a lovely place)
Such a lovely face.
They livin' it up at the Hotel California
What a nice surprise (what a nice surprise), bring your alibis
Mirrors on the ceiling,
The pink champagne on ice
And she said, 'we are all just prisoners here, of our own device'
And in the master's chambers,
They gathered for the feast
They stab it with their steely knives,
But they just can't kill the beast
Last thing I remember, I was
Running for the door
I had to find the passage back to the place I was before
'Relax' said the night man,
'We are programmed to receive.
You can check out any time you like,
But you can never leave!'
>>> s = 'c:\next\trans\edit\new.day'
>>> s
'c:\next\trans\\edit\new.day'
>>> print(s)
c:
ext	rans\edit
ew.day
>>> print(s, sep='')
c:
ext	rans\edit
ew.day
>>> print(r
KeyboardInterrupt
>>> print(r'c:\next\trans\edit\new.day')
c:\next\trans\edit\new.day
>>> print("{s}".format(s))
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    print("{s}".format(s))
KeyError: 's'
>>> print("{s}".format(s="Hellow"))
Hellow
>>> print("{s}".format(s=s))
c:
ext	rans\edit
ew.day
>>> c
'On a dark desert highway, cool wind in my hair\nWarm smell of colitas, rising up through the air\nUp ahead in the distance, I saw a shimmering light\nMy head grew heavy and my sight grew dim\nI had to stop for the night.\nThere she stood in the doorway;\nI heard the mission bell\nAnd I was thinking to myself\n\'This could be heaven or this could be Hell\'\nThen she lit up a candle and she showed me the way\nThere were voices down the corridor,\nI thought I heard them say\nWelcome to the Hotel California\nSuch a lovely place (such a lovely place)\nSuch a lovely face.\nPlenty of room at the Hotel California\nAny time of year (any time of year) you can find it here\nHer mind is Tiffany-twisted, she got the Mercedes bends\nShe got a lot of pretty, pretty boys, that she calls friends\nHow they dance in the courtyard, sweet summer sweat\nSome dance to remember, some dance to forget\nSo I called up the Captain,\n\'Please bring me my wine\'\nHe said, \'we haven\'t had that spirit here since nineteen sixty-nine\'\nAnd still those voices are calling from far away,\nWake you up in the middle of the night\nJust to hear them say"\nWelcome to the Hotel California\nSuch a lovely place (such a lovely place)\nSuch a lovely face.\nThey livin\' it up at the Hotel California\nWhat a nice surprise (what a nice surprise), bring your alibis\nMirrors on the ceiling,\nThe pink champagne on ice\nAnd she said, \'we are all just prisoners here, of our own device\'\nAnd in the master\'s chambers,\nThey gathered for the feast\nThey stab it with their steely knives,\nBut they just can\'t kill the beast\nLast thing I remember, I was\nRunning for the door\nI had to find the passage back to the place I was before\n\'Relax\' said the night man,\n\'We are programmed to receive.\nYou can check out any time you like,\nBut you can never leave!\''
>>> f.readline()
''
>>> f.tell()
1822
>>> len(c)
1777
>>> f.seek(0)
0
>>> f.readline()
'On a dark desert highway, cool wind in my hair\n'
>>> f.readline()
'Warm smell of colitas, rising up through the air\n'
>>> f.readline()
'Up ahead in the distance, I saw a shimmering light\n'
>>> for i in range(5):
	f.readline()

	
'My head grew heavy and my sight grew dim\n'
'I had to stop for the night.\n'
'There she stood in the doorway;\n'
'I heard the mission bell\n'
'And I was thinking to myself\n'
>>> f.seek(0)
0
>>> c = f.readlines()
>>> c
['On a dark desert highway, cool wind in my hair\n', 'Warm smell of colitas, rising up through the air\n', 'Up ahead in the distance, I saw a shimmering light\n', 'My head grew heavy and my sight grew dim\n', 'I had to stop for the night.\n', 'There she stood in the doorway;\n', 'I heard the mission bell\n', 'And I was thinking to myself\n', "'This could be heaven or this could be Hell'\n", 'Then she lit up a candle and she showed me the way\n', 'There were voices down the corridor,\n', 'I thought I heard them say\n', 'Welcome to the Hotel California\n', 'Such a lovely place (such a lovely place)\n', 'Such a lovely face.\n', 'Plenty of room at the Hotel California\n', 'Any time of year (any time of year) you can find it here\n', 'Her mind is Tiffany-twisted, she got the Mercedes bends\n', 'She got a lot of pretty, pretty boys, that she calls friends\n', 'How they dance in the courtyard, sweet summer sweat\n', 'Some dance to remember, some dance to forget\n', 'So I called up the Captain,\n', "'Please bring me my wine'\n", "He said, 'we haven't had that spirit here since nineteen sixty-nine'\n", 'And still those voices are calling from far away,\n', 'Wake you up in the middle of the night\n', 'Just to hear them say"\n', 'Welcome to the Hotel California\n', 'Such a lovely place (such a lovely place)\n', 'Such a lovely face.\n', "They livin' it up at the Hotel California\n", 'What a nice surprise (what a nice surprise), bring your alibis\n', 'Mirrors on the ceiling,\n', 'The pink champagne on ice\n', "And she said, 'we are all just prisoners here, of our own device'\n", "And in the master's chambers,\n", 'They gathered for the feast\n', 'They stab it with their steely knives,\n', "But they just can't kill the beast\n", 'Last thing I remember, I was\n', 'Running for the door\n', 'I had to find the passage back to the place I was before\n', "'Relax' said the night man,\n", "'We are programmed to receive.\n", 'You can check out any time you like,\n', "But you can never leave!'"]
>>> type(c)
<class 'list'>
>>> c[0]
'On a dark desert highway, cool wind in my hair\n'
>>> c[1]
'Warm smell of colitas, rising up through the air\n'
>>> c[-1]
"But you can never leave!'"
>>> c[10, 30]
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    c[10, 30]
TypeError: list indices must be integers or slices, not tuple
>>> c[10:30]
['There were voices down the corridor,\n', 'I thought I heard them say\n', 'Welcome to the Hotel California\n', 'Such a lovely place (such a lovely place)\n', 'Such a lovely face.\n', 'Plenty of room at the Hotel California\n', 'Any time of year (any time of year) you can find it here\n', 'Her mind is Tiffany-twisted, she got the Mercedes bends\n', 'She got a lot of pretty, pretty boys, that she calls friends\n', 'How they dance in the courtyard, sweet summer sweat\n', 'Some dance to remember, some dance to forget\n', 'So I called up the Captain,\n', "'Please bring me my wine'\n", "He said, 'we haven't had that spirit here since nineteen sixty-nine'\n", 'And still those voices are calling from far away,\n', 'Wake you up in the middle of the night\n', 'Just to hear them say"\n', 'Welcome to the Hotel California\n', 'Such a lovely place (such a lovely place)\n', 'Such a lovely face.\n']
>>> f.tell()
1822
>>> f.close()
>>> f
<_io.TextIOWrapper name='C:\\Users\\Purushotham\\Desktop\\Clients\\HPE\\HPEB02\\day04\\hc.txt' mode='r' encoding='cp1252'>
>>> f.read()
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    f.read()
ValueError: I/O operation on closed file.
>>> f = open(r"C:\Users\Purushotham\Desktop\Clients\HPE\HPEB02\day04\wrtest.txt", "w")
>>> f.write('HOTEL CALIFORNIA LYRICS\n\n')
25
>>> content = ['Original: Eagles\n', 'Cover by: HPEB02\n'])
SyntaxError: invalid syntax
>>> content = ['Original: Eagles\n', 'Cover by: HPEB02\n']
>>> f.writelines(content)
>>> f.close()
>>> len(
KeyboardInterrupt
>>> len('HOTEL CALIFORNIA LYRICS\n\n')
25
>>> src = open(r"C:\Users\Purushotham\Desktop\Clients\HPE\HPEB02\day04\hc.txt", "r")
>>> dest = open(r"C:\Users\Purushotham\Desktop\Clients\HPE\HPEB02\day04\wrtest.txt", "a")
>>> dest.write('\n\n')
2
>>> line = 0
>>> while True:
	line = src.readline()
	if(line == ''):
		break
	else:
		line = line.upper()
		dest.write(line)

		
47
49
51
41
29
32
25
29
45
51
37
27
32
42
20
39
57
56
61
52
45
28
26
69
50
39
23
32
42
20
42
63
24
26
66
30
28
39
35
29
21
57
28
31
37
25
>>> src.close()
>>> dest.close()
>>> for i in range(10):
	print(i, end='')

	
0123456789
>>> src = open(r"C:\Users\Purushotham\Desktop\Clients\HPE\HPEB02\day04\hc2.txt", "r")
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    src = open(r"C:\Users\Purushotham\Desktop\Clients\HPE\HPEB02\day04\hc2.txt", "r")
FileNotFoundError: [Errno 2] No such file or directory: 'C:\\Users\\Purushotham\\Desktop\\Clients\\HPE\\HPEB02\\day04\\hc2.txt'
>>> '12' + 12
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    '12' + 12
TypeError: can only concatenate str (not "int") to str
>>> D = {}
>>> D['name']
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    D['name']
KeyError: 'name'
>>> 3/0
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    3/0
ZeroDivisionError: division by zero
>>> 
 RESTART: C:/Users/Purushotham/Desktop/Clients/HPE/HPEB02/day04/exceptions.py 
>>> 
