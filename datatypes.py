Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#datatypes
a=2
type(a)
<class 'int'>
b=5.9
type(b)
<class 'float'>
c='python'
type(c)
<class 'str'>
d="course"
type(d)
<class 'str'>
e="'vinay"'
SyntaxError: incomplete input
e='''vinay'''
type(e)
<class 'str'>
f=5+9j
type(f)
<class 'complex'>
h=True
type(h)
<class 'bool'>
i=False
type(i)
<class 'bool'>
print(a,b,c,d,e)
2 5.9 python course vinay
#dataytype conversion
int(5)
5
int(3.4)
3
int('python')
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    int('python')
ValueError: invalid literal for int() with base 10: 'python'
int(4+9j)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    int(4+9j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(True)
1
int(False)
0
#float
float(5)
5.0
float(4.5)
4.5
float(4+5j)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    float(4+5j)
TypeError: float() argument must be a string or a real number, not 'complex'
>>> float(True)
1.0
>>> float(False)
0.0
>>> float("vinay")
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    float("vinay")
ValueError: could not convert string to float: 'vinay'
>>> #str
>>> str(3)
'3'
>>> str(3.4)
'3.4'
>>> str("vinay")
'vinay'
>>> str(4+9j)
'(4+9j)'
>>> str(True)
'True'
>>> str(False)
'False'
>>> #complex
>>> complex(9)
(9+0j)
>>> complex(4.5)
(4.5+0j)
>>> complex("vinay")
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    complex("vinay")
ValueError: complex() arg is a malformed string
>>> complex(True)
(1+0j)
>>> complex(False)
0j
>>> #bool
>>> bool(3)
True
>>> bool(3.34)
True
>>> bool(3+4j)
True
>>> bool(True)
True
>>> bool(False)
False
