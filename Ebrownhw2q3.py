n=int(input("Enter the height:"))
if n%2==0:
    n=int(input("Please enter an odd number:"))


print(' '*(n)+'*')
for i in range(1, n+1):
    if i>n//2:

        print(' '*(n-i)+'*'+' '*(2*i-1)+'*')

if n>1:
    print(' '*n+'*')
