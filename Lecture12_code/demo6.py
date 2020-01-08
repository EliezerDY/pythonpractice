a = [1,2,3]
b = "abc"
c = zip(a,b)
d = list(c)
print(d)
c = zip(a,b)
for i in c:
  print(i,end=" ")
c = zip(a,b)
d = [i for i in c]
print(d)
