#if-condition by using comparision operators
#<,>,<=,>=,!=,==
'''a=10
b=20
if a<b:
    print("true")'''

'''a=40
b=60
if a>b:
    print("less")'''

'''a=50
b=80
if b>a:
    print("greater")'''

'''a=11
b=13
if b>=a:
    print("greater")'''

'''a=7
b=8
if a!=b:
    print("not equal")'''

'''a=5
b=5
if a==b:
    print("equal")'''

'''a="python"
if a=="python":
    print("true")'''

'''a="java"
if a!="python":
    print("false")'''

'''a=int(input("a value"))
b=int(input("b value"))
if a<b:
    print("less")'''

'''a=int(input("a value"))
if a>30:
    print("true")'''

#if-condition by using logical operators
#and,or,not

'''a=4
b=8
if a<b and b>a:
    print("less")'''

'''a=6
b=9
if a<=b and b>=a:
    print("true")'''

'''a=7
b=10
if a!=b and b==a:
    print("less")'''

'''a=12
b=14
if a<b or b>a:
    print("less")'''

'''a=15
b=20
if a<=b or b>=a:
    print("true")'''

'''a=10
b=20
if a!=b or b==a:
    print("less")'''

'''a=3
b=5
if not a<b:
    print("true")'''

#if-condition by using identify operators
#is,is not

'''a=10
if type(a) is int:
    print("it is int")'''

'''a=7
if type(a) is not int:
    print("false")'''

'''a=10.3
if type(a) is not int:
    print("is not int")'''

'''a=int(input("a value"))
if type(a) is int:
    print("true")'''

#if-condition by using membership operators
#in, not in

'''a=[2,3,4,5,6,7,8,9,10]
if 5 in a:
    print("true")'''

'''a=[2,3,4,5,6,7,8,9,10]
if 10 not in a:
    print("true")'''

'''a=[2,3,4,5,6,7,8,9,10]
if 15 not in a:
    print("true")'''

'''a=[2,3,4,5,6,7,8,9,10]
b=int(input("enter the value: "))
if b in a:
    print("true")'''

#if-else conditions by using comparision operators

'''a=5
b=9
if a<b:
    print("less")
else:
    print("false")'''

'''a=5
b=9
if a>b:
    print("less")
else:
    print("false")'''

'''a=3
b=5
if a!=b:
    print("true")
else:
    print("false")'''
#tasks
'''a=4
b=4
if a==b:
    print("false")
else:
    print("true")'''

'''a=5
b=6
if a<b or b>a:
    print("true")
else:
    print("false")'''

'''a=5
b=8
if a<b and b<a:
    print("true")
else:
    print("false")'''

'''a=4
if type(a) is int:
    print("true")
else:
    print("false")'''

'''a=3.4
if type(a) is float:
    print("true")
else:
    print("false")'''

a=[2,3,4,5,6,7,8,9,10]
b=int(input("enter the value: "))
if b in a:
      print("true")
else:
    print("false")
