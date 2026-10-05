#local variables and global variables

#1. a variable is defined inside and outside the function is called global and local variables.
#2. a variable is defined inside the function and is accessible to the entire global space is called global variables.
#3. a varibale is defined inside the function is called local variable.

#first case of global variable
'''a=4
def check():
    print("inside value is",a)
check()
print("outside value is",a)'''

#second case of global variable
'''a=5
def check1():
    a=10
    a=a**2
    print("inside value is",a)
check1()'''

#third case of global variable
'''a=3
b=2
def check2():
    a=8
    print("inside value is",a)
    a=10
    print("inside value is",a+5)
    b=12#local variable
    b=b+a
    print("inside b value is",b)
check2()
print("a value is",a)
print("b value is",b)'''

#usage of global keyword

#when user wants to create a variable inside the function directly and carry forward the "updated" value even outside the function
#then we need to use global keyword.
a=4
def final():
    global a,b
    print("inside value is",a)
    a=7
    print("updated value is",a)
    #global b
    b=13
    b=b+a
    print("b value is",b)
final()
print("a value is",a)
print("b value is",b)






































