# functions
# import math
#log math .log
# print(math.log10(100))
#pi -fixed value
# print(math.pi)
#sqrt -know this
# print(math.sqrt(100))
#pow -two input
# print(math.pow(5,2))

# import with from
#ex1 -square root from user input:
# n = int(input("Enter a #:"))
# print(math.sqrt(n))

#ex2 -fourth root:
# n = int(input("Enter a #:"))
# print(math.sqrt(math.sqrt(n)))

#ex3:
# n1 = int(input("Enter a #:"))
# n2 = int(input("Enter a second #:"))
# print(math.pow(n1,n2))
#ex4:
# n = int(input("Enter a #:"))
# print(math.pow(n,1/3))

#create own functions
#demo-no result because function not called
# def my_function():
#     print("Hello from function")
#call function-prints the message
# my_function()
#demo of func. with parameters
# def my_function(fname):
#     print("Hello from function")
#     print(fname)
#must put in argument for fname
# my_function("week8")

#default parameters -not everyone needs parameters
# my_function("Sweden")
# my_function("India")
# my_function()
# my_function("Brazil")

# parameters and arguments
# def my_function(country):
#     a ="person"
#     print("I am from " + country)
# # local variable
#     # print(a)
# my_function("Sweden")
# my_function("India")
# # my_function()
# my_function("Brazil")

# return values
# def my_function(x):
#     return 5 * x
#     # need print value to print the value
# print(my_function(3))
# print(my_function(5))
# print(my_function(9))

# more examples
import math
#
# def area(radius):
#  return math.pi * radius**2
#
# def abso_value(x):
#   if x<0:
#     return -x
#   else:
#     return x
#
# print(area(abso_value(-10)))
#             # what will it print?
#             # pi10^2

# know for test how to predict what the answer of this code will be
# code terminates when condition is fulfilled, rest is ignored
# fruitful (or nonvoid) function
# def f1(a):
#     if a >0 and a<10:
#         return a * 10
#     if a>100 and a < 1000:
#         return a//10
#     return a *2
# print (f1(5)) #50
# print (f1(150))#15
# print (f1(50))#100

# keyword arguments
# def func(child3, child2, child1):
#     print("The youngest is:" + child3)
#
# func(child1 ="Emil", child2 ="Tobias", child3 = "Linus")

#arbitrary arguments  add star
# def func(*kids):
#     print("The youngest is:" + kids[0])
#
# func("Emil", "Tobias", "Linus")
# func("a")
# func("a", "b")

# composition
# import math
# def area(radius):
#   return math.pi * radius ** 2
#
# def distance(xc,yc,xp,yp):
#   math.sqrt(math.pow(xc-xp,2)+math.pow(yc-yp,2))
#
#
# def circle_area(xc,yc,xp,yp):
#   radius = distance(xc,yc,xp,yp)
#   result = area(radius)
#   return result
#
# print(circle_area(1,2,-1,-5))

# boolean functions -True or False, capitalize
# def is_div(x,y):
#     if x%y ==0:
#         return True
#     else:
#         return False
# print(is_div(6,4))

# pass statement
# def f1():
#     pass
# f1()

# ex:5-functions
def printHello():
    print("Hello")

printHello()

# ex:6
# import math
def circleArea(r):
    return math.pi *r**2

print(circleArea(10))

# ex:7
def displayReverse(n):
    while n>0:
        print(n%10)
        n = n//10

displayReverse(1234)

#ex:8
def numberToTens(n):
    r =1
    while n>9:
        r =r*10
        n =n//10
    return r

print(numberToTens(54321))

# ex:9
def factorial(n):
    r =1
    for i in range(1, n+1):
        r =r*i
    return r
print(factorial(5))

#ex:10

# def prime (n):
#     for i in range (2,n):
#         if n%i==0:
#             return False
#     else:
#         return True
#
# def aftn(n):
#     while  prime(n)==False:
#         n +=1
#     return n
#
# print(aftn(1000000000))

# another version
# import math
#
# def prime (n):
#     for i in range (2,math.ceil(math.sqrt(n))+1):
#         if n%i==0:
#             return False
#     else:
#         return True
#
# def aftn(n):
#     while  prime(n)==False:
#         n +=1
#     return n
#
# print(aftn(1000000000))

#ex.11
# import math
#
# def quad(a,b,c):
#     x1 = (-b+ math.sqrt(b**2 - 4 * a *c))/(2*a)
#     x2 = (-b- math.sqrt(b**2 - 4 * a *c))/(2*a)
#     return x1,x2
# a = float(input("Enter a:"))
# b = float(input("Enter b:"))
# c = float(input("Enter c:"))
#
# x1,x2 = quad(a,b,c)
# print("x1 =", x1)
# print("x1 =", x2)

#  RANDOM NUMS demo
import random
# seed -will always be same sequence
# random.seed(0)
a=random.random()
print(a)
# demo 2
import random
a=random.random()
print(a)
for i in range(10):
    print(random.random())
# demo 3 - random uniform
a=random.random()
print(a)
for i in range(10):
    print(random.uniform(1,10))
print("------------")
#  random radint
for i in range(10):
    print(random.randint(1,10))
print("------------")
# divisible by third number
for i in range(10):
    print(random.randrange(1,101,2))
print("------------")
#
# ex.12 -KNOW FOR TEST!!!!
import random
for i in range(10):
    print(random.randint(1,6))

# ex.13
def sfac(n):
    r =0
    for i in range(1,n+1):
      r+=i
    return r
n =int(input("Enter a num:"))
print(sfac(n))

# ex.14
def sfac(n):
    for i in range(2,n+1):
        if n%i==0:
            f=i
            break
    return f
n = int(input("Enter a num:"))
print(sfac(n))

# ex.15
def reverse(n):
    r =0
    while n>0:
        r =r*10 + n%10
        n //=10
    return r

n = int(input("Enter a num:"))
print(reverse(n))
