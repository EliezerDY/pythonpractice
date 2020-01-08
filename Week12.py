# tuples -parentheses
thistuple =("apple", "banana", "cherry")
print(thistuple)
print(thistuple[0])
print(thistuple[-1])
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# range of index
print(thistuple[2:5])
# loop through tuple
for i in thistuple:
    print(i,end =" ")
if "apple" in thistuple:
    print("apple is in tuple")
# cant change item in tuple, must convert to list first
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)
# length
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
# type
print(type(thistuple))#prints list
# tuple in list
a=[(1,2),(3,4)]
print(a)
a[0] =(2,5)
print(a)
# list inside tuple
b =([1,2,3],[4,5,6])
print(b)
# cant modify the list for it has tuples, however to modify the list works
b[0][0]=2
print(b)
# tuple with one element
a =("apple",)
print(type(a))
# th following is just a string
b =("apple")
print(b)
print(type(b))
# when deleted the tuple is gone
# del a
# print(a)
# join tuples with plus
tuple1 =("a", "b", "c")
tuple2 =(1,2,3)
tuple3 =tuple1 + tuple2
print(tuple3)
# tuple methods
# count how many a's in the tuple
a =("a", "b", "c", "a")
print(a.count('a'))
# get index num.
print(a.index('a'))
# swapping values
a =1
b =2
temp =a
a =b
b =temp
print(a,b)
a,b =b,a
print(a,b)
# split
a,b = "David, Tom".split(",")
print(a,b)
#functions
def f(n1,n2):
    a =n1*2
    b =n2*3
    return (a,b)

(a1,a2) = f(10,20)
print(a1,a2)#20,60
a1 =50
a2 =30
print(a1,a2)
# or\
a =f(20,30)
print(a)#(40,90)
# zip
a =[1,2,3]
b ="abc"
c =zip(a,b)
for i in c:
  print(i,end=" ")
  #
 # d =[i for i in c]
 # print(d)
 # compare tuples
 # print((1,2,3))<(2,3,4)
 # print((1,9,9))<(2,3,4)
 # print((1,9,9,0))<(1,9,9)

# ex1
from statistics import mean, variance, stdev
# import math
# import statistics
def stat(a):
    return max(a), min(a),mean(a),variance(a),stdev(a)
    # return max(a),min(a),statistics.mean(a),statistics.variance(a),statistics.stdev(a)
print(stat([1,2,3,4,5]))
