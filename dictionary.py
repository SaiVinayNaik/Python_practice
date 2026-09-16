Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#dictionary => dict{}
a={"name":"Vinay","city":"vja"}
print(a)
{'name': 'Vinay', 'city': 'vja'}
type(a)
<class 'dict'>
b={"name","vinay"}
type(b)
<class 'set'>
#keys()
a={"year":2026,"month":"sep","date":9}
a.keys()
dict_keys(['year', 'month', 'date'])
#values()
a.values()
dict_values([2026, 'sep', 9])
#items()
a.items()
dict_items([('year', 2026), ('month', 'sep'), ('date', 9)])
a["year"]
2026
#get()
a.get()
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    a.get()
TypeError: get expected at least 1 argument, got 0
a.get(year)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    a.get(year)
NameError: name 'year' is not defined
a.get("year")
2026
#update
a={"name":"Vinay Naik","city":"Vij"}
a.update({"mailid":"Vinaynaik@gmail.com"})
a
{'name': 'Vinay Naik', 'city': 'Vij', 'mailid': 'Vinaynaik@gmail.com'}
a.update({"Year":2026},{"Time":3})
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    a.update({"Year":2026},{"Time":3})
TypeError: update expected at most 1 argument, got 2
a.update({"Year":2026,"Time":03:00})
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
a.update({"Year":2026,"Time":3:00})
SyntaxError: invalid syntax
a.update({"Year":2026,"Time":3})
A
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    A
NameError: name 'A' is not defined. Did you mean: 'a'?
a
{'name': 'Vinay Naik', 'city': 'Vij', 'mailid': 'Vinaynaik@gmail.com', 'Year': 2026, 'Time': 3}
#setdefault()
a={"hour":3,"min":10}
a.setdefault("sec",4)
4
a
{'hour': 3, 'min': 10, 'sec': 4}
#pop()
a={"week":"wed","date":9}
a.pop("week")
'wed'

a
{'date': 9}
#popitems()
a={"Country":"India","state":"ap"}
a.popitem()
('state', 'ap')
a
{'Country': 'India'}
#copy()
a={"Name":"Vinay","Course":"Python":"Duration":100}
SyntaxError: invalid syntax
a={"Name":"Vinay","Course":"Python","Duration":100}
a.copy()
{'Name': 'Vinay', 'Course': 'Python', 'Duration': 100}
a
{'Name': 'Vinay', 'Course': 'Python', 'Duration': 100}
len(a)
3
a.count("Name")
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    a.count("Name")
AttributeError: 'dict' object has no attribute 'count'
a.index("course")
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    a.index("course")
AttributeError: 'dict' object has no attribute 'index'
a.clear()
a
{}
#duplicates
a={"name":"vinay","year":"2026","name":"vinay"}
a
{'name': 'vinay', 'year': '2026'}
a={"name":"vinay","year":2026,"name":"naik"}
a
{'name': 'naik', 'year': 2026}
a={"name":"vinay","year":2026,"name1":naik}
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    a={"name":"vinay","year":2026,"name1":naik}
NameError: name 'naik' is not defined
a
a={"name":"vinay","year":2026,"name1":"naik"}
a
{'name': 'vinay', 'year': 2026, 'name1': 'naik'}
#key,value,items()
a={"idnos":[10,20,30],"names":["sai","vinay","naik"],"courses":["c","python","java"]}
a
{'idnos': [10, 20, 30], 'names': ['sai', 'vinay', 'naik'], 'courses': ['c', 'python', 'java']}
a.keys()
dict_keys(['idnos', 'names', 'courses'])
a.values()
dict_values([[10, 20, 30], ['sai', 'vinay', 'naik'], ['c', 'python', 'java']])
type(a)
<class 'dict'>
a.items()
dict_items([('idnos', [10, 20, 30]), ('names', ['sai', 'vinay', 'naik']), ('courses', ['c', 'python', 'java'])])
#tasks
a=["code","codegnan","python"]
a.upper()
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    a.upper()
AttributeError: 'list' object has no attribute 'upper'
a.[upper()]
SyntaxError: invalid syntax
upper(a)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    upper(a)
NameError: name 'upper' is not defined. Did you mean: 'super'?
.upper(a)
SyntaxError: invalid syntax
a.upper[()]
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    a.upper[()]
AttributeError: 'list' object has no attribute 'upper'
a.upper(["code","codegnan","python"])
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    a.upper(["code","codegnan","python"])
AttributeError: 'list' object has no attribute 'upper'
a.upper("code","codegnan","python")
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    a.upper("code","codegnan","python")
AttributeError: 'list' object has no attribute 'upper'
a.upper["code","codegnan","python"]
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    a.upper["code","codegnan","python"]
AttributeError: 'list' object has no attribute 'upper'
a.upper(["code"],["codegnan"],["python"])
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    a.upper(["code"],["codegnan"],["python"])
AttributeError: 'list' object has no attribute 'upper'
>>> b=str(a)
>>> b.upper()
"['CODE', 'CODEGNAN', 'PYTHON']"
>>> #task2
>>> a=[9,1,5,2,8,4,6,3,7,0]
>>> a.sort(reverse)
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    a.sort(reverse)
NameError: name 'reverse' is not defined. Did you mean: 'reversed'?
>>> a.sort()
>>> a
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> a.reverse()
>>> a
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
>>> a=[9,1,5,2,8,4,6,3,7,0]
>>> a1=a[0:5]
>>> a1
[9, 1, 5, 2, 8]
>>> a2=a[5:10]
>>> a2
[4, 6, 3, 7, 0]
>>> a1.sort()
>>> a1
[1, 2, 5, 8, 9]
>>> a2.sort()
>>> a2
[0, 3, 4, 6, 7]
>>> a1.reverse()
>>> a1
[9, 8, 5, 2, 1]
>>> a2.reverse()
>>> a2
[7, 6, 4, 3, 0]
>>> c=a1+a2
>>> c
[9, 8, 5, 2, 1, 7, 6, 4, 3, 0]
