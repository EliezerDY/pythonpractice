a = [1,2,3]
b = ["a","b","c","d"]
c = dict(zip(b,a))
print(c)
for i in c:
    print(i,c[i])

for i,j in c.items():
    print(i,j)
