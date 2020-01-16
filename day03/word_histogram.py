text = '''
There's a hero
If you look inside your heart
You don't have to be afraid
Of what you are
There's an answer
If you reach into your soul
And the sorrow that you know
Will melt away
And then a hero comes along
With the strength to carry on
And you cast your fears aside
And you know you can survive
So when you feel like hope is gone
Look inside you and be strong
And you'll finally see the truth
That a hero lies in you
It's a long road 
When you face the world alone
No one reaches out a hand
For you to hold
You can find love
If you search within yourself
And that emptiness you felt 
Will disappear
And then a hero comes along
With the strength to carry on
And you cast your fears aside
And you know you can survive
So when you feel like hope is gone
Look inside you and be…
'''

print(text)

words = text.split()
hist = {}
for word in words:
    if(word not in hist.keys()):
        hist[word] = words.count(word)


print('WORD HISTOGRAM: ')
print(hist)


