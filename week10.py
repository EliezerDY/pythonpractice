# # lists (no arrays)
# #demo1
# a =[10,20,30,40]
# # access with bracket operator
# print(a[2])
# print(a[3])
# print(a)
# # list inside list-returns inner list
# b = ['spam', 2.0, 5, [10,20]]
# print(b[0])
# print(type (a[3]))
# # call multiple in one step
# print(b[0], b[2], b[3])
# print(b[3])
# # negative index -print backword
# print(b[-1])
# # renge of index-get part of array group with colon(include first,not last)
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon"]
# print(thislist[2:5])
# print(thislist[1:3])
# # use negative
# print(thislist[-4:-1])
# # to include last or first (if neg or pos respective ,) element, no index
# print(thislist[-4:])
# print(thislist[:-1])
# # give whole list
# print(thislist[:])

# demo2
# traverse lists

# a =[10,20,30,40,50,60,70,80,90,100]
# print element divided by 10
# for i in a:
#     print(i//10)
#     i = i*10
# print(a)
# print elementnumber  and divided by 10
# for i in range (len(a)):
#     print(i,"=",a[i])
    # a[i] =a[i] * 10
# modify list value
# print(a)

# demo3
# concantinate lists
# a =[1,2,3]
# b=[4,5,6]
# c =a +b
# # new list of both combined
# print(c)
# # pint 1,2,3 three times
# d =a*3
# print(d)
# # print 100 i's in array
# e =[1] *100
# print(e)

# IMPORTANT -methods
# demo4
# check if item in list
# a =[10,20,30,40,50,60,70,80,90,100]
# print((20 in a))#returns true
# print((20 in a))#returns false
# # check length  of list
# print(len(a))
# b =[]
# print(len(b))
# # add item,append
# b.append("Apple")
# print(b)
# # insert in middle of list
# a.insert(2,25)
# print(a)
# # remove items
# c= ["orange", "kiwi", "kiwi","pinapple"]
# c.remove("kiwi")#only removes 1 kiwi
# print(c)
# # pop method to remove specific index
# # with out any index, last element is removed
# a.pop()
# print(a)
# # remove 70
# a.pop(7)
# print(a)
# # delete (del) method also removes
# del a[1]
# print(a)
# # clear empties list
# a.clear()
# print(a)

# demo5
# copy
# a =[10,20,30,40,50,60,70,80,90,100]
# b =a
# print(b)
# # what's done to list a will also affect b
# a[0]=100
# print(b)
# # overcome with list
# c =[10,20,30,40,50,60,70,80,90,100]
# d = list(c)
# c[0] =20
# print(c)
# print(d)
# extend methods-joins lists

# demo6
# a =["a", "b", "c"]
# b =[1,2,3]
# a.extend(b)
# print(a)
# # convert string to list

# # demo7
# a ="span-span-span"
# # character seperation
# b = list(a)
# print(b)
# # use split
# c = a.split('-')
# print(c)
# a = "abc def ghk"
# # no need to put in argument to split by space
# d = a.split()
# print(d)
# # list to string

# # demo8
# a =["apple", "banana", "cherry"]
# # first one is diliniator
# b = " ".join(a)
# print(b)

# ex.1
# a =[4,5,3,10,9]
# r =0
# for i in a:
#     r+=i
# print(r//len(a))
# # or
# print(sum(a)//len(a))

# ex.2
# a =[4,5,3,10,9]
# b =["Max", "Freddy", "Kelly", "Bob", "Jack"]
# c =a +b
# a.extend(b)
# print(a)
# print(c)

# ex.3
# entrie = input("Enter 11 numbers: ")
# userList = entrie.split()
# int(userList)
# r =0
# for i in userList:
#     r+=i
# print(r//len(userList))
# input_string = input("Enter a list numbers or elements separated by space: ")
# userList = input_string.split()
# print("user list is ", userList)
#
# print("Calculating sum of element of input list")
# sum = 0
# for num in userList:
#     sum += int(num)
# print("Sum = ", sum)


# know for test
# ex:9 -biggest value plus first index
# a =[2,1,4,3,11,6,7,11,8,9,10]
# a =[6,12,14,7,8,9]
# greatest =a[0]
# largest_index =0
# for i in range(len(a)):
#     if greatest <a[i]:
#         greatest = a[i]
#         largest_index = i
# print("The largest value is:", greatest)
# print("The index of the largest value is:", largest_index)

# ex:10
# a =[1,1,3,4,4,4,7,8,8,8]
# # if (len(a)>0)
# c =1
# e =a[0]
# for i in a:
#     if e !=i:
#         e =i
#         c+=1
# print("There are", c,"distinct elements")

# ex:11
# a =[1,2,3,4,5,6,7,8,9]
# for i in range(0,len(a)-1,2):
#     temp =a[i]
#     a[i] =a[i+1]
#     a[i+1]=temp
# for i in a:
#     print(i,end=" ")

#ex:12
# a =[1,2,3,4,5,6,7,8,9]
#
# smallest_index =0
# largest_index =0
# for i in range(len(a)):
#     if a[largest_index]<a[i]:
#         largest_index=i
#     if a[smallest_index]>a[i]:
#         smallest_index =i
# temp = a[largest_index]
# a[largest_index] =a[smallest_index]
# a[smallest_index]=temp
#
# for i in a:
#     print(i,end =" ")

# ex:13 -VERY HARD
# a =[1,2,3,4,,5,6,7,8,8]
# c =0
# for i in range(len(a)):
#     for j in range(len(a)):
#         if a[i] != None and a[i] ==a[j] and i!=j:
#             c+=1
#             a[i] =None
#             a[j] =None
# print("Number of equal pair:", c)

# ex:16
def minArray(a):
    min =a[0]
    for i in a:
        if min >i:
            min =i
    return min
a =[3,4,5,2,3]
print(minArray(a))

# ex:17
def avgArray(a):
    avg =0
    for i in a:
        avg+=i
    return avg/len(a)
a =[3,4,5,2,3]
print(avgArray(a))
