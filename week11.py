# nested lists -two odimensional array
# demo 1
# a =[[1,2,3], [4,5,6]]
# print(a[0])
# print(a[1])
# b =a[0]
# print(b) #assign b to a [1,2,3]
# print(a[0][2])
# a[0][1] =7
# print(a)#[[1,7,3] [4,5,6]]
# print(b)#1,7,3
# b[2]=9
# print(a[0])
# print(b)

# demo 2
# print 2D arrays
# a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
# for i in range(len(a)):
#  for j in range(len(a[i])):
#    print(a[i][j], end=' ')
#  print()

 # demo 3
 # trace by element
#  a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
# for row in a:
#  for elem in row:
#    print(elem, end=' ')
#  print()

# demo4
# calculate sums
# a= [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
# s = 0
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         s += a[i][j]
# print(s)
# # add only even numbers (know for exam)
# a= [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
# s = 0
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         if a[i][j]%2==0:
#             s += a[i][j]
#
# print(s)
# # demo5
# # make multiply even numbers by two fails , can only do
# # using retrieve by index for elem is merely a copy and can't change original
# a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
# for row in a:
#  for elem in row:
#   if elem%2==0:
#       elem =elem*2
# print(a)

def make2dList(rows, cols):
    return [ ([0] * cols) for row in range(rows) ]

rows = 3
cols = 2

a = make2dList(rows, cols)

print("This IS ok.  At first:")
print("   a =", a)
