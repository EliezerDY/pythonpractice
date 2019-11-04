# n=int(input("Enter the height:"))
# if n%2==0:
#     n=int(input("Please enter an odd number:"))
#
# # j=n
# # print(' '*(n)+'*')
# for i in range(1, n+1):
#     # for j in range(1, n+1):
#     if i>n//2:
#     # if i>n:
#     #     print(' '*(i-n)+'*'+' '*(2*j-1)+'*')
#     #     j-=1
#     # else:
#         #print(' '*n+'*')
#        print(' '*(n-i)+'*'+' '*(2*n-i)+'*')
#     # else:
#     #    print(' '*(n-i)+'*')
# # if i>n//2:
#     # print(' '*n+'*')
###################################3
n=int(input("Enter the height:"))
if n%2==0:
    n=int(input("Please enter an odd number:"))
# j=n-1
print(' '*(n)+'*')
for i in range(1, n+1):
    if i>n:
        print(' '*(i-n)+'*'+' '*(2*j-1)+'*')
        # j-=1
    else:
        print(' '*(n-i)+'*'+' '*(2*i-1)+'*')
if n>1:
    print(' '*n+'*')
