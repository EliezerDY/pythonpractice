#1
a = input("Enter a word of five letters:")
if (len(a)!=5):
    print("Invalid input")
    exit()
print(a)
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
#2
a = ("This is a test string")
#slicer
print(a[0:4])
print(a[5:7])
print(a[8:9])
print(a[10:14])
print(a[15:22])
# second way =split
b = a.split(" ")
print(b[0])
print(b[1])
print(b[2])
print(b[3])
print(b[4])
#3
a = ("this isQCC!")
print(a)
print(a[0:7] + " " + a[7:11])
b = (a.replace("t", "T"))
print(b[0:7] + " " + a[7:11])
print(b[0:7] + " " + a[7:10])
print(b[0:7] + " the City University of New York")
print(b[0:7] + " the City University of New York.")
#3 -professor
a = ("this isQCC!")
a =a.replace("isQCC", "is QCC")
print(a)
a = a.replace("this", "This")
print(a)
a = a[:-1]
print(a)
a = a.replace("QCC", "the City University of New York")
print(a)
a = a + "."
print(a)
