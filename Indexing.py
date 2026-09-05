Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #indexing
>>> a="vijayawada"
>>> a[5]
'a'
>>> a[13]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    a[13]
IndexError: string index out of range
>>> b="I am vinay"
>>> b[3]+b[5]
'mv'
>>> z="I am vinay"
>>> z[-5]+z[-4]+z[-3]+z[-2]+z[-1]
'vinay'
