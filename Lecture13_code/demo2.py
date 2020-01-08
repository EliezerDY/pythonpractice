a = {"apple", "banana", "cherry"}
a.add("orange")
print(a)
a.add("orange")
print(a)
#a[0] = "pear"
a.update(["orange", "mango", "grapes"])
print(a)
b = {1,1,2,3,4,4}
print(b)
print(len(a))
b.remove(1)
print(b)
a.discard("banana")
print(a)
a.pop()
print(a)
b.clear()
print(b)
