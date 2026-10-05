#ASCII
#CHR,ORD
'''print(chr(65))
print(chr(90))
print(chr(92))
print(ord("a"))
print(ord("z"))'''
#print(ord(98)) in ord we won't give numbers
#print(chr("a") in chr we won't give letters

#task1
'''for i in range(65,91):
    print(chr(i),end=" ")
    
for i in range(97,123):
    print(chr(i),end=" ")'''

name=input("name")
for i in name:
    print(i,"-",ord(i))
