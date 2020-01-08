n = int(input("Enter a Number:"))
for i in range(n-1,0,-1):
    if n%i == 0:
        print("Largest factor:",i)
        break
