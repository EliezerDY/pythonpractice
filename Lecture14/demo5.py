a = {"a":2,"b":4,"c":"d",2:"a"}
print(("a" in a))
print(("d" in a))
print(len(a))
print(a[2])
a["e"]=5
print(len(a))
a["e"]=6
a.pop("e")
print(len(a))
a[5]="a"
print(len(a))
a["5"]="a"
print(len(a))
a["2"]=(1,2,3)
print(a)
