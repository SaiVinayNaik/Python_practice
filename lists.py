Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#list[]
a=[3,4.5,"python",3+4j,True,False]
print(a)
[3, 4.5, 'python', (3+4j), True, False]
type(a)
<class 'list'>
b=4.5
print(b)
4.5
type(b)
<class 'float'>
c=[4.5]
type(c)
<class 'list'>
#append list
a=["python","java","c"]
a.append("sql")
a
['python', 'java', 'c', 'sql']
a.append("ml","ai")
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    a.append("ml","ai")
TypeError: list.append() takes exactly one argument (2 given)
a.append(["ml","ai"])
a
['python', 'java', 'c', 'sql', ['ml', 'ai']]
#extend list
a=["c","java","python"]
a.extend("sql","c++")
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    a.extend("sql","c++")
TypeError: list.extend() takes exactly one argument (2 given)
a.extend(["sql","c++"])
a
['c', 'java', 'python', 'sql', 'c++']
#insert list
a=["black","white"]
a.insert(1,"blue")
a
['black', 'blue', 'white']
#index list
a=["apple","banana","carrot"]
a.index("carrot")
2
a.extend(["pomogranate"])
a
['apple', 'banana', 'carrot', 'pomogranate']
a.index("pomogranate")
3
#pop list
a=["hi","hello","how","are","you"]
a.pop()
'you'
a
['hi', 'hello', 'how', 'are']
a.pop(3)
'are'
a
['hi', 'hello', 'how']
a.extend(["bye","thank you"])
a
['hi', 'hello', 'how', 'bye', 'thank you']
#remove
a.remove("hello")
a
['hi', 'how', 'bye', 'thank you']
#sort
a=["vij","hyd","bng","chn","vzg"]
a.sort()
a
['bng', 'chn', 'hyd', 'vij', 'vzg']
b=[9,40,24,2,5,1]
b.sort()
b
[1, 2, 5, 9, 24, 40]
#reverse
a=["mango","banana","carrot","berry"]
>>> a.reverse()
>>> a
['berry', 'carrot', 'banana', 'mango']
>>> b=[10,4,5,3,84,7]
>>> b.reverse()
>>> b
[7, 84, 3, 5, 4, 10]
>>> #len()
>>> a=["c","c++","java"]
>>> len(a)
3
>>> b="java"
>>> len(b)
4
>>> c=["java"]
>>> len(c)
1
>>> a.count("c")
1
>>> #clear()
>>> a=["python","java","c"]
>>> a.clear()
>>> a
[]
>>> a.append("vinay")
>>> a
['vinay']
>>> a.extend("helo","learning","python")
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    a.extend("helo","learning","python")
TypeError: list.extend() takes exactly one argument (3 given)
>>> a.extend(["helo","learning","python"])
>>> a
['vinay', 'helo', 'learning', 'python']
>>> a.pop(1)
'helo'
>>> a
['vinay', 'learning', 'python']
