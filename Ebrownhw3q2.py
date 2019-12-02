def gcd2(a,b):
    if b ==0:
        return a
    return gcd2(b,a%b)
a,b =input("Enter two integers:").split()
a= int(a)
b=int(b)
print("The GCD of", a, "and", b, "is", +gcd2(a,b))
