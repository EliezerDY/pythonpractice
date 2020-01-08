#while loops
i =1
while i<6:
    print(i)
    i = i + 1
#print to 100
i =1
while i<101:
    print(i)
    i = i + 1
    #with input
n =int(input("Enter number:"))
i =1
while i<=n:
    print(i)
    i= i + 1
    # run until user enters positive #
n = int(input("Enter positive #:"))
while n<=0:
    n =int(input("Try again:"))
    print("You entered positive #")
    #break statement
    i = 1
    while i<6:
        print(i)
        if i ==3:
         break
        i+=1
