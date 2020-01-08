x = input("Pick a number (0 if odd, 1 if even):")
x =float(x)
if (x % 2 ==0):
     print("1\n")
else:
    print("0\n")
#2
n = input("Write a number (1 if not multiple of 5, 0 if multiple):")
num =int(n)
if(num %5 ==0):
    print("1\n")
else:
    print("0\n")
#3
x = input("Pick a number (1 if multiple of 3 and not of 7):")
x =float(x)
if (x % 3 ==0 and x % 7 !=0):
     print("1\n")
else:
    print("0\n")
#4
x =input("Type a number:")
x =int(x)
if(x %2 !=0 and x<=20 or x>50):
    print(1)
else:
    print(0)
#5
x =input("Enter a number")
x =int(x)
if(x %2 ==0):
   print(x, "is even")
#6
x = input("Enter number:")
x =int(x)
if(x % 5==0):
   print(x,"is multiple of 5")
if (x % 3==0):
   print(x,"is multiple of 3")
if (x%5==0 and x%3==0):
    print(x, "is multiple of 5", x, "is multiple of 3")
#7
movies = input ("Do you want to go to movies (1/0)")
dinner= input("Do you want to go to dinner (1/0)")
movies =bool(int(movies))
dinner = bool(int(dinner))
if movies == True and dinner ==False:
    print("You are going to movies")
elif movies == False and dinner == True:
    print("You are going to dinner")
elif movies ==True and dinner ==True:
    print("Can't do both")
else:
    print("You must do something")
#8
rain = input("Is it raining (1/0)")
rain = int(rain)
if rain == 1:
    activity = input("Do 1) Watch TV or 2) Do homework?")
    activity= int(activity)
    if activity ==1:
        print("Watch TV")
    elif activity ==2:
        print("Do homework")
    else:
        print("Non valid entry")
elif rain ==1:
    activity = input("Do 1) Hit beach or 2) Go to museum?")
    activity = int(activity)
    if activity ==1:
        print("Hit beach")
    elif activity ==2:
        print("Go to museum")
    else:
        print("Non valid entry")
 #9
x =input("Enter value and see if valid:")
x =int(x)
if(x>50 or x<0):
   print(x, "is valid.")
else:
    print(x, "is not valid.")
#10
x = input("Enter number 1:")
y = input("Enter number 2:")
z = input("Enter number 3:")
x =int(x)
y =int(y)
z =int(z)
print("input 1:", x, "\n","input 2:", y, "\n","input 3:", z)
if (x >= y) and (x >= z) and (y > z):
   print("Max to min ", x, y, z)
elif (x >= y) and (x >= z) and (z > y):
   print("Max to min ", x, z, y)
elif (y >= x) and (y >= z) and (x > z):
   print("Max to min ", y, x, z)
elif (y >= x) and (y >= z) and (z > x):
   print("Max to min ", y, z, x)
elif (z >= x) and (z >= y) and (y > x):
   print("Max to min ", z, y, x)
else:
   print("Max to min ",z, x, y)
