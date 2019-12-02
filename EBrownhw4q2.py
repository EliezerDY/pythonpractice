NumList = []
Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
    value = (input("Enter the character of Element %d: " %i))
    NumList.append(value)
print("Original:", NumList)
for i in range(len(NumList)-1,-1,-1):

  print( NumList[i])
