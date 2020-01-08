a = [1,1,2,3,4,5,2,4,1]
b = [2,4,5,8,9,1,2,4,3]
c = a + b
d = set(c)
print(len(d))

e = set(a)
f = set(b)
g = e.union(f)
print(len(g))
