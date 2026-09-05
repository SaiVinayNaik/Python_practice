Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Operators
#Arithematic
a,b=2,4
print(a+b)
6
print(a-b)
-2
print(a*b)
8
print(a//b)
0
print(a/b)
0.5
print(a**b)
16
print(a%b)
2
#Assignments
a,b=3,6
a+=b
b
6
b-=a
b
-3
b*=a
b
-27
b//=4
b
-7
b**=10
b
282475249
b%=1
b
0
#comparision
x,y=8,10
x<y
True
x>y
False
y<x
False
y>x
True
x!=y
True
x<=y
True
y<=x
False
x>=y
False
y>=x
True
x==y
False
x,y=10,10
x==y
True
#logical
l,m=5,10
l<m and m>l
True
l>m and m>l
False
l<=m and m>==l
SyntaxError: invalid syntax
l<=m and m>=l
True
l<m or m<l
True
l<m or m>l
True
l>m or m>l
True
l<=m or m>=l
True
#identify
k=8
type(k) is int
True
type(k) is not int
False
j='vinay'
type(j) is not string
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    type(j) is not string
NameError: name 'string' is not defined
type(j) is not str
False
>>> type(k)is float
False
>>> #membership
>>> a=2,3,4,5,6,7,8,9
>>> 10 in a
False
>>> 4 in a
True
>>> #bitwise
>>> a,b=3,4
>>> a&b
0
>>> c,d=6,3
>>> c&d
2
>>> a,b=9,7
>>> a|b
15
>>> x,y=3,5
>>> x|y
7
>>> a=5
>>> ~a
-6
>>> l=10
>>> ~l
-11
>>> a,b=6,8
>>> a^b
14
>>> x,y=4,9
>>> x^y
13
>>> a=9
>>> a<<2
36
>>> a=5
>>> a<<3
40
>>> a=3
>>> a>>2
0
>>> a=7
>>> a>>2
1
>>> a,b=4,5
>>> a&b
4
