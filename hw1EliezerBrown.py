#1
print("Change Calculator\n-----------------" )
money = float(input("Enter dollar amount:"))
quarters = money*100//25
dimes = (money *100 % 25) // 10
nickels = money *100 % 25 % 10 // 5
pennies = money *100 % 25 % 10 % 5
print("The equivalent in coins:")
print(quarters, "Quarters")
print(dimes, "Dimes")
print(nickels, "Nickels")
print(pennies, "Pennies:")


#2
A = int(input("Please enter the value of A:"))
B = int(input("Please enter the value of B:"))
C = int(input("Please enter the value of C:"))
X = int(input("Please enter the value of X:"))
E = A*(X**2)+B*X+C
print("The value of equation A*(X**2)+B*X+C is",E,".")

#3
firstname = input("Enter your first name:")
lastname = input("Enter your last name:")
fullname = firstname + " " + lastname
print ("Your full name is", fullname)
print("Length:", len(fullname))
middle = input("Enter your middle initial:")
fullname =firstname + " "+"{}"+ " " +lastname
print("Your full name is " + fullname.format(middle))
initial =firstname[:1] + "." +middle+ "."+lastname[:1]+"."
print("Your initials name is " + initial)

#4
age =int(input("Please enter age your age:"))
if age <18:
    print("You are too young to vote.")
elif age <18 or age >75:
    print("You can't drive.")
elif age >=18:
    reg = int(input("Did you register to vote? (1 for yes /0 for no)"))
    if reg ==1:
         print("You can vote.")
    else:
       print("You must register before you can vote.")

#5
grade = float(input("Enter your grade:"))
if (grade>=96 and grade <=100):
       print("You will receive a letter grade of A with a 4.00 GPA")
elif (grade>=90 and grade <=95):
        print("You will receive a letter grade of A- with a 3.70 GPA")
elif (grade>=87 and grade <=89):
        print("You will receive a letter grade of B+ with a 3.30 GPA")
elif (grade>=84 and grade <=86):
         print("You will receive a letter grade of B with a 3.00 GPA")
elif (grade>=80 and grade <=83):
       print("You will receive a letter grade of B- with a 2.70 GPA")
elif (grade>=77and grade <=79):
         print("You will receive a letter grade of C+ with a 2.30 GPA")
elif (grade>=74 and grade <=76):
        print("You will receive a letter grade of C with a 2.00 GPA")
elif (grade>=70 and grade <=73):
          print("You will receive a letter grade of C- with a 1.70 GPA")
elif (grade>=67 and grade <=69):
         print("You will receive a letter grade of D+ with a 1.30 GPA")
elif (grade>=64 and grade <=66):
           print("You will receive a letter grade of D with a 1.00 GPA")
elif (grade>=60 and grade <=63):
           print("You will receive a letter grade of D- with a 0.70 GPA")
elif (grade>=0 and grade <=59):
           print("You will receive a letter grade of F with a 0.00 GPA")
else:
    print("You have not entered a grade between 0 and 100. Ending program.")
exit()
