num = input("Pick a number between 0 to 100:")
x =int(num)
if(x>=0 and x<=100):
    f = 9/5 *x +32
else:
    exit()
print("The number in Celcius", x, "in Fahrenheit",f)
#2
num = input("Enter number:")
x =int(num)
if(x % 3==0 and x%5!=0):
   print("The result is", x/3)
elif (x % 5==0 and x%3!=0):
   print("The result is", x/5)
elif (x%5==0 and x%3==0):
    print("The result is", x/3/5)
else:
    print("The number", x, "is not what we want")
