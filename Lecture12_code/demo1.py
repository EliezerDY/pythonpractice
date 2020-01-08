thistuple = ("apple", "banana", "cherry", "orange", "kiwi")
print(thistuple)
print(thistuple[0])
print(thistuple[-1])
print(thistuple[1:3])
print(thistuple[-3:-1])
#thistuple[0]="pear"
for i in thistuple:
    print(i,end=" ")
if "apple" in thistuple:
    print("\nYes, 'apple' is in the fruits tuple")
print(len(thistuple))
#thistuple[5] = "orange"
print(type(thistuple))
print(type([]))

a = ("apple",)
print(type(a))
b = ("apple")
print(type(b))
del a
