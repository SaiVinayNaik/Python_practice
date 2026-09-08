Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#tuple
a=(3,5.4,"vinay",3+4j,True,False)
print(a)
(3, 5.4, 'vinay', (3+4j), True, False)
type(a)
<class 'tuple'>
len(a)
6
a.count(3+4j)
1
a.index(True)
4
#sets
a={3,4.5,"python",4+6j,True,False}
a
{False, True, 3, 4.5, (4+6j), 'python'}
type(a)
<class 'set'>
b={0,4,6,3,76,3,6,4,3}
b
{0, 3, 4, 6, 76}
#set is a un order, set will not allow duplicate values.
#add
a={4,5,6,7,8,9}
a.add(10)
a
{4, 5, 6, 7, 8, 9, 10}
#subset
a={4,5,6,7,8,9}
b={7,8,9}
b.issubset(a)
True
a.issubset(b)
False
#superset
a={6,7,8,9,10,11,12}
b={10,11,12}
a.issuperset(b)
True
b.issuperset(a)
False
#union
a={3,4,5,6,7}
b={5,6,7,8,9,10}
a.union(b)
{3, 4, 5, 6, 7, 8, 9, 10}
#intersection()
a={10,11,12,13,14,15}
b={14,15,16,17}
a.intersection(b)
{14, 15}
b.intersection(a)
{14, 15}
#update
a={2,3,4,5,6,7,8}
b={5,6,7,8,9,10}
a.update(b)
a
{2, 3, 4, 5, 6, 7, 8, 9, 10}
a
{2, 3, 4, 5, 6, 7, 8, 9, 10}
b.update(a)
b
{2, 3, 4, 5, 6, 7, 8, 9, 10}
print(a,b)
{2, 3, 4, 5, 6, 7, 8, 9, 10} {2, 3, 4, 5, 6, 7, 8, 9, 10}
#difference
a={6,7,8,9,10,11}
b={2,3,4,5,6,7,8}
a.difference(b)
{9, 10, 11}
b.difference(a)
{2, 3, 4, 5}
#symmetric
a={7,8,9,10,11,12,13}
b={10,11,12,13,14,15}
a.symmetric_difference(b)
{7, 8, 9, 14, 15}
#difference update
a={3,4,5,6,7,8}
b={4,5,6,7,8,9,10}
a.difference_update(b)
a
{3}
b.difference_update(a)
b
{4, 5, 6, 7, 8, 9, 10}
#intersection_update
a={3,4,5,6,7,8}
b={1,3,6,7,8,9,10}
a.intersection_update(b)
a
{8, 3, 6, 7}
a
{8, 3, 6, 7}
b.intersection_update(a)
b
{8, 3, 6, 7}
#symmetric_difference_update
a={6,7,8,9,10,11,12}
b={10,11,12,13,14,15}
a.symmetric_difference_update(b)
a
{6, 7, 8, 9, 13, 14, 15}
b.symmetric_difference_update(a)
b
{6, 7, 8, 9, 10, 11, 12}
#pop_list
>>> a={10,20,30,40,50}
>>> a.pop()
50
>>> a
{20, 40, 10, 30}
>>> a.pop()
20
>>> a
{40, 10, 30}
>>> a.remove(10)
>>> a
{40, 30}
>>> #discard
>>> a={4,5,6,7,8,9}
>>> a.discard(8)
>>> a
{4, 5, 6, 7, 9}
>>> #copy
>>> a.copy()
{4, 5, 6, 7, 9}
>>> a
{4, 5, 6, 7, 9}
>>> b=a.copy()
>>> b
{4, 5, 6, 7, 9}
>>> #clear
>>> a={3,4,5,6,7}
>>> a.clear()
>>> a
set()
>>> #disjoint
>>> a={3,4,5,6,7,8}
>>> b={2,3,4,6,7}
>>> a.isdisjoint(b)
False
>>> a={6,7,8,9}
>>> b={1,2,3,4}
>>> a.isdisjoint(b)
True
