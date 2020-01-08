a = [1,1,2,3,4,5,2,4,1,10,11,12]
b = [2,4,5,8,9,1,2,4,3]
c = a + b
d = set(c)
a1 = set(a)
b1 = set(b)
e = []
for i in d:
    if i in a1 and i in b1:
        e.append(i)
e.sort()
print(e)
