l1 = [1,2,3]
l2 = l1
l1[1]=10
print(l2)
a = {"a":2,"b":4,"c":"d",2:"a"}
b = a.copy()
a["a"]=5
print(b)

s1 = set(l1)
print(s1)
t1 = tuple(l1)
print(t1)
c = dict(a)
print(c)
