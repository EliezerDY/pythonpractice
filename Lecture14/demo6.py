a = {"a":2,"b":4,"c":"d",2:"a"}
print(a.pop("a"))
a.popitem()
print(a)
del a["b"]
print(len(a))
a.clear()
print(a)
print(type(a))
