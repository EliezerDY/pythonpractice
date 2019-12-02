x =1
y= 1
if x==y:
  print("x and y are equal")
else:
  print("x and y aren't equal")
a =2
b =3
if a> b:
     print("a bigger than b")
elif a ==b:
    print("a is equal to b")
else:
    print("a smaller than b")
# grade ex1
grade =input("What's your grade?")
grade =int(grade)
if (grade>90):
  print("A")
elif (grade>80):
 print("B")
elif (grade>70):
  print("C")
elif (grade<70):
   print("F")
  # grade ex 2
grade =input("What's your grade?")
grade =int(grade)
if (grade>97):
       print("A+")
elif (grade>90):
        print("A")
elif (grade>93):
       print("A")
elif (grade>90):
        print("A-")
elif (grade>87):
         print("B+")
elif (grade>83):
       print("B")
elif (grade>80):
         print("B-")
elif (grade>77):
        print("C+")
elif (grade>73):
          print("C")
elif (grade>70):
         print("C-")
elif (grade<70):
           print("F")

#ex 1
n = input("Pick a number:")
n =float(n)
if (n % 2 ==0):
     print("The number is even")
else:
    print("The number is odd\n")
#2
n = input("Write a number:")
num =int(n)
if(num %7 ==0):
    print("The number is divisible by seven")
else:
    print("The number isn't divisible by seven\n")
#3
age =input("What is your age?")
age = int(age)
if(age<0):
    print("You are idiot")
else:
    sec = age*365*24*60
    print("Your age is", age, "you are",sec, "seconds old.")
