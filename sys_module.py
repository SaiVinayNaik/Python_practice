#sys module
'''import sys
print(sys.path)'''

'''for i in sys.path:
    print(i)
print(sys.version)'''

#os module
import os
#print(os.path)
#print(os.getcwd())
#print(os.listdir())
#print(os.mkdir("oct5"))
#print(os.listdir())
#print(os.chdir("C:\Users\hp\Desktop\Python Course\sep2\oct5"))

#random module - is used to generate random numbers in python, randint function{} is used and this function is defined random module
#1.sample
'''import random
a=random.sample(range(10,50),5)
print(a)'''

#2.randint()
'''import random
a=random.randint(5,12)
print(a)'''

#3.choice
'''import random
a=[10,20,30,40,50]
b=random.choice(a)
print(b)'''

#calender module
'''import calendar
year=2026
month=10
print(calendar.month(year,month))'''

'''import calendar
year=2027
print(calendar.calendar(year))'''

'''import calendar
a=int(input("enter the year"))
b=int(input("enter the month"))
print(calendar.month(a,b))'''

#date & time
'''from datetime import date
a=date.today()
print(a)'''

'''import datetime
a=datetime.datetime.now()
print(a)'''

import time
a=time.time()
print(a)#epoch time
b=time.localtime(a)
print(b)
print(f"today date is{b.tm_mday}-{b.tm_mday}-{b.tm_mon}-




























