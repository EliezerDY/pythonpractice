a = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# print one after another
for i in a:
    print(i)
# print keys with values
for i in a:
    print(i,a[i])
# another way
for i,j in a.items():
    print(i,j)
