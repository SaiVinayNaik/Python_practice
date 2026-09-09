Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=10
>>> print(a)
10
>>> A=10
>>> print(a)
10
>>> del a
>>> print(a)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print(a)
NameError: name 'a' is not defined. Did you mean: 'A'?
>>>  s=9
...  
SyntaxError: unexpected indent
>>> name = "vinay"
>>> print(name)
vinay
>>> print(vinay)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print(vinay)
NameError: name 'vinay' is not defined
>>> 9s=10
SyntaxError: invalid decimal literal
>>> country="india"
>>> print(country)
india
>>> Name="vinay"
>>> print(name)
vinay
>>> $=5
SyntaxError: invalid syntax
>>> 9=30
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
>>> fname=vinay
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    fname=vinay
NameError: name 'vinay' is not defined
>>> fname="vinay"
>>> lname="naik"
>>> print(fname+" "+lname)
vinay naik
>>> if=90
SyntaxError: invalid syntax
