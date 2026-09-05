Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#slicing
a="codegnan"
a[0:4]
'code'
b="vinay"
b[0:6]
'vinay'
z="work until you succeed"
z[5:10,15:22,11:14,0:4]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    z[5:10,15:22,11:14,0:4]
TypeError: string indices must be integers, not 'tuple'
z[5:10] [15:22] [11:14] [0:4]
''
z[5:10]
'until'
z[15:22]
'succeed'
z[11:14]
'you'
z[0:4]
'work'
k="Happy Teachers Day"
k[-13:-18]
''
k[-18:-13]
'Happy'
k[-3:0]
''
k[-3:-1]
'Da'
k[-3:1]
''
k[-3:1]
''
k[:-3]
'Happy Teachers '
k[-3:]
'Day'
k[-12:-4]
'Teachers'
j="Vizag is a city of Destiny"
j[-26:-21]
'Vizag'
>>> j=[-15:-11]
SyntaxError: invalid syntax
>>> j[-15:-11]
'city'
>>> j[-26:-21]
'Vizag'
>>> j[-7:]
'Destiny'
>>> #strding
>>> a="Data Science"
>>> a[::]
'Data Science'
>>> a[::2]
'Dt cec'
>>> a="Machine learning"
>>> a[::3]
'Mheeng'
>>> a[::5]
'Mnag'
>>> a[::2]
'Mcielann'
>>> a[::9]
'Me'
>>> a[3:11]
'hine lea'
>>> m="Cloud Computing"
>>> m[2:13:3]
'o mt'
>>> m[4:14:5]
'dp'
>>> m[3:12:6]
'up'
>>> l="Python Course"
>>> l[[-1:-9:-3]
...   
SyntaxError: invalid syntax
>>> l[-1:-9:-3]
...   
'eu '
>>> l[-2:-12:-4]
...   
'sCh'
>>> l[-4:-13:-5]
...   
'uo'
>>> l[-6:-12:-2]
...   
'Cnh'
