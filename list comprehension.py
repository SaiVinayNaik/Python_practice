#list comprehension
'''every list comprehension is can be rewritten as a for loop but every for loop cannot be rewritten in list comprehension'''
#["PYTHON","JAVA","DSA"]
a=["PYTHON","JAVA","DSA"]
#print(a.upper())

'''for i in a:
    print(i.upper(),end=" ")'''
'''b=[]
for i in a:
    b.append(i.upper())
print(b)'''

#syntax
#a=[expr for var in collection/range]
'''b=[i.upper() for i in a]
print(b)'''

'''b=["apple","mango"]
#["APPLE","MANGO"]
b=[i.capitalize() for i in b]
print(b)'''

#[1,4,9,25,36,64,144,169]
'''a=[1,2,3,4,5,6,8,12,13]
b=[i**2 for i in a]
print(b)'''

'''a=[i for i in range(0,21)]
print(a)'''

#if-usage in list comprehension
'''a=[i for i in range(16) if i%2==0]
print(a)'''

'''a=[i**2 for i in range(31) if i%2==0]
print(a)'''

'''a=["grapes","berry","mango","kiwi","dragon","apple"]
for i in a:
    if "a" not in i:
        print(i)'''

#no-elif usage in list comprehension
#if-else usage in list comprehension
'''a=[i**2 if i%2==0 else i*5 for i in range(21)]
print(a)'''

'''a=[1,2,3,4,5]
b=[5,4,3,2,1]
#[6,6,6,6,6]
c=[a[i]+b[i] for i in range (len(a))]
print(c)'''

#max(),min(),sum()
'''print(max(2,4,5,8,7,5,20,135,22))'''
'''print(min(333,4444,2,35,1,0.3,343))'''
#print(sum(2,3))
a=3,4,5,2,2,5,34
print(sum(a))























