print("1) Summation of 1 to n inclusive.")
print("2) n! (n factorial)")
print("3) Exit program")
option = int(input("Select:"))
while option != 3:
    if option == 1:
        n = int(input("Enter a value for n (n must be between 1 and 11): "))
        while n<1 or n>11:
            print("Invalid input.")
            n = int(input("Enter a value for n (n must be between 1 and 11): "))
        r = 0
        for i in range(n+1):
          r += i
        print("1 to",n,"summation =",r)
    elif option == 2:
        n = int(input("Enter a value for n (n must be between 1 and 11): "))
        while n<1 or n>11:
            print("Invalid input.")
            n = int(input("Enter a value for n (n must be between 1 and 11): "))
        r = 1
        for i in range(1,n+1):
          r *= i
        print(n,"Factorial =",r)
    else:
        print("Invalid option")
    print("1) Summation of 1 to n inclusive.")
    print("2) n! (n factorial)")
    print("3) Exit program")
    option = int(input("Select:"))
else:
    print("Ending Program")
