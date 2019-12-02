NumList = []

for i in range(5):
    value = int(input("Please enter the Value of  Element %d: " %i))
    NumList.append(value)

smallest = largest = NumList[0]

for j in range(1, 5):
    if(smallest > NumList[j]):
        smallest = NumList[j]
        min_position = j
    if(largest < NumList[j]):
        largest = NumList[j]
        max_position = j
print("List:", NumList)
print("Max: ", largest)
print("Min: ", smallest)
