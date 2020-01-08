# recursive functions
# non recursive factorial
# def f1(n):
#     r =1
#     for i in range(1,n+1):
#         r *=i
#     return  r
# print(f1(5))
# # using recursion
# def f2(n):
#     if n ==1:
#         return 1
#     return n*f2(n-1)
# print(f2(5))

# ex2:
# non-recursive
# def num_dig1(n):
#     c =0
#     while n >0:
#         n//=10
#         c+=1
#     return c
# print(num_dig1(1234))
# # recursive
# def num_dig2(n):
#     if n <10:
#         return 1
#     return 1+num_dig2(n//10)
# print(num_dig2(1234))

# wx3:
# non-recursive
# def fdig1(n):
#     while n>10:
#       n//=10
#     return n
# print(fdig1(1234))
# # recursive
# def fdig2(n):
#     if n < 10:
#       return n
#     return fdig2(n//10)
# print(fdig2(1234))

# ex4:
# non-recursive
# def sum_ev1(n):
#     r =0
#     while n>0:
#         r+=n%10
#         n//=10
#     return r
# print(sum_ev1(1234))
# # recursive
# def sum_ev2(n):
#     if n<10:
#         return n
#     return n%10 + sum_ev2(n//10)
# print(sum_ev2(1234))

# ex5:
# non-recursive
# def ninreverse1(n):
#         while n >0:
#             print(n%10)
#             n//=10
# ninreverse1(1234)
# # recursive
# def ninreverse2(n):
#     if n<10:
#         print(n)
#     else:
#         print(n%10)
#         ninreverse2(n//10)
# ninreverse2(1234)
# ex:6
# def rfirstdig(n):
#     # deal with first number
#     if n<10:
#         return 0
#     return n%10 + 10 * rfirstdig(n//10)
# print(rfirstdig(1234))
# # ex:7
# def remzero(n):
#     if n<10:
#         return n
#     elif n%10==0:
#         return remzero(n//10)
#     else:
#         return n%10 + 10 *remzero(n//10)
#
# print(remzero(1042))

#ex8:-sum of (triangle)
# def tri(n):
#     r =0
#     for i in range(1,n+1):
#         r+=i
#     return r
# print(tri(5))
# recursive
# def tri2(n):
#      if n==1:
#          return 1
#      return n+tri2(n-1)
# print(tri2(5))

# 9 -fibonacci numbers
# def fib(n):
#    if n == 1 or n==2:
#        return 1
#    return fib(n-1)+fib(n-2)
# print(fib(5))
# print(fib(10))
# print(fib(15))
# print(fib(20))

# 10-gcf
# def gcd1(a,b):
#     for i in range (a,2,-1):
#         if a%i ==0 and b%i == 0:
#             return i
#     return 1
#
# def gcd2(a,b):
#     if b ==0:
#         return a
#     return gcd2(b,a%b)
#
# print(gcd1(300,500))
# print(gcd1(49,140))
# print(gcd2(49,140))
# print(gcd2(300,500))

# 11-palindrome
# def pal(s):
#     if len(s)==0 or len(s)==1:
#         return True
#     elif s[0]!= s[-1]:
#         return False
#     else:
#         return pal(s[1:-1])
#
#
# print(pal("noon"))
# print(pal("dad"))
# print(pal("mom"))
# print(pal("rear"))#false
# print(pal("car")) #false
