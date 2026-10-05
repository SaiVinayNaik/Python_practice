'''while True:
    a=input("a value")
    b=input("b value")
    print(a+b)'''

'''while True:
    a=eval(input("a value"))
    b=eval(input("b val"))
    print(a+b)'''

#zip() -> we can combine multiple collections into one collection
'''a=[10,20,30,40,50]
names=["sai","vinay","naik","ramu","raju"]
print(a+names)
b=zip(a,names)
print(b)
c=list(zip(a,names))
print(c)
d=tuple(zip(a,names))
print(d)
e=set(zip(a,names))
print(e)
f=dict(zip(a,names))
print(f)'''

#enumerate()->we can give counter to the collection
'''names=["hi","helo","ok","good","bad"]
for i in range(len(names)):
    print(i,names[i])
b=list(enumerate(names))
print(b)
b=list(enumerate(names,10))
print(b)
c=set(enumerate(names,10))
print(c)
d=dict(enumerate(names,20))
print(d)'''

#anonymous functions->anonymous functions are nameless functions and we use a keyword called as 'lambda' to create anonymous function.
'''def f(x):
    print(2*x+5)
f(5)'''

'''def f():
    x=int(input("value"))
    print(2*x+5)
f()'''

#syntax
#a=lambda arg:expr
'''a=lambda x:2*x+5
print(a(5))'''

'''a=int(input("enter a value"))
b=lambda x:2*x+5
print(b(a))'''

'''a=lambda x,y:x*y
print(a(4,5))'''

'''a="python"
#PYTHON
b=lambda a:a.upper()
print(b(a))'''

'''b=lambda a:a.upper()
print(b("python"))'''

'''a=input("fname")
b=input("lname")
c=lambda a,b:a+" "+b
print(c(a,b))'''

a,b=[x for x in input("names").split(",")]
c=lambda a,b:(a+" "+b).title()
print(c(a,b))
























