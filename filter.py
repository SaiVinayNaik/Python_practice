#filter()
#a[2,6,7,9,10,






#[],(),set()
'''a=[]
print(type(a))

b=()
print(type(b))

c={}
print(type(c))

d=set()
print(type(d))'''

'''a=[[],(),set(),{}," ",None,3,5.6,"python",9+3j,True,False]
b=list(filter(None,a))
print(b)'''

#map()-> each object from a acollection and forms a new li
'''a=[2,4,6,8,10,12,15,20,25]
b=[1,5,3,0,4,20,25,30,60,80]
c=list(map(max,a,b))
print(c)'''

'''a=[2,4,6,8,10,12,15,20,25]
b=[1,5,3,0,4,20,25,30,60,80]
c=list(map(min,a,b))
print(c)'''

#run_time input()
'''a=int(input("a value"))
b=int(input("b value"))
print(a+b)'''

'''a,b=[int(x) for x in input("values").split(",")]
print(a+b)'''

'''a,b=int(input("enter the values").split(","))
print(a+b)'''#error

'''a,b=map(int,input("enter the values").split(","))
print(a+b)'''

'''a=input("data1")
b=input("data2")
print(a+b)'''

'''a,b=[x for x in input("data").split(",")]
print(a+b)'''

'''a,b=input("data").split(",")
print(a+b)'''

'''a=list(map(int,input("data").split(",")))
print(a)'''

'''a,b=map(str,input("data").split(","))
print(a+b)'''

'''a=tuple(map(int,input("data").split(",")))
print(a)'''

'''a=set(map(int,input("data").split(",")))
print(a)'''

'''a=list(map(str,input("data").split(",")))
print(a)'''

'''a=list(map(eval,input("data").split(",")))
print(a)'''

'''a=list(map(int,input("data").split(",")))
print(a)'''

'''a=input("enter the key and value pairs")
b=dict(i.split(":") for i in a.split(","))
print(b)'''






























