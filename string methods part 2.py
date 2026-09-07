Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#replace
a="wait until you succeed"
a.replace("wait","work")
'work until you succeed'
b="python java"
b.replace("java","c")
'python c'
#upper()
a="python"
a.upper()
'PYTHON'
#lower()
b="JAVA"
b.lower()
'java'
#capitalize()
c="programming"
c.capitalize()
'Programming'
#title()
d="programming language"
d.title()
'Programming Language'
#small conditions
a="hello world"
a.startswith("h")
True
a.endswith("d")
True
a.isalpha() #no space in bw words it wont consider
False
b="helloworld"
b.isalpha()
True
a.isdigit()
False
b=3456
b.isdigit() #wont consider as digits cause python is case sensitive it should always in string type
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    b.isdigit() #wont consider as digits cause python is case sensitive it should always in string type
AttributeError: 'int' object has no attribute 'isdigit'
b="2345"
b.isdigit()
True
d="Python"
d.isalnum() #either alphabet or number
True
e="3456"
e.isalnum()
True
#strip()
#lstrip(),rstrip()
a=
SyntaxError: incomplete input
a="          pooja          "
a.strip()
'pooja'
a.lstrip()
'pooja          '
a.rstrip()
'          pooja'
#concatenation
a="code"
b="gnan"
print(a+b)
codegnan
a="programming"
b="language"
print(a+" "+b)
programming language
fname="Vinay"
lname="Naik"
print(fname+" "+lname)
Vinay Naik
fname="sai"
mname="vinay"
lname="naik"
print((fname+" "+mname+" "+lname).title())
Sai Vinay Naik
#split()
a="python java c c++ sql"
a.split()
['python', 'java', 'c', 'c++', 'sql']
b="I am learning python fullstack"
b.split()
['I', 'am', 'learning', 'python', 'fullstack']
i="vja","hyd","vzg"
"".join(b)
'I am learning python fullstack'
"".join(i)
'vjahydvzg'
" ".join(i)
'vja hyd vzg'
"k".join(i)
'vjakhydkvzg'
c="hello"
"m".join(c)
'hmemlmlmo'
#formatting
a=5
b=7
print(a+b)
12
print("the sum is",a+b)
the sum is 12
city="vja"
print("city is",city)
city is vja
#format
a=
SyntaxError: incomplete input
a="vinay"
b="naik"
print("hello {}{}".format(a,b))
hello vinaynaik
print("hello {} {}".format(a,b))
hello vinay naik
>>> print("hello {} hello{}".format(a,b))
hello vinay hellonaik
>>> print("hello {} hello {}".format(a,b))
hello vinay hello naik
>>> #fstring()
>>> a="Ramu"
>>> b="Naik"
>>> print(f"hello {a}{b}")
hello RamuNaik
>>> print(f"hello {a} {b}")
hello Ramu Naik
>>> print(f"hello {a} hello{b}")
hello Ramu helloNaik
>>> print(f"hello {a} hello {b}")
hello Ramu hello Naik
>>> #Task
>>> #Task1
>>> fname="vinay"
>>> lname=
SyntaxError: incomplete input
>>> lname="naik"
>>> print("hello {fname} {lname}")
hello {fname} {lname}
>>> print(f"hello {fname} {lname}")
hello vinay naik
>>> #task2
>>> a=2
>>> b=5
>>> print("the sum is {} + {}".format(a,b))
the sum is 2 + 5
>>> print("the sum is {}".format(a+b))
the sum is 7
>>> a=5
>>> b=4
>>> c=a+b
>>> print("the sum is {c}")
the sum is {c}
>>> print(f"the sum is {c}")
the sum is 9
