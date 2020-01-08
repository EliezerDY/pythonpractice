def frequency_word(s):
    d = dict()
    l = s.split()
    for w in l:
        if w not in d:
            d[w]=1
        else:
            d[w] += 1
    return d

print(frequency_word("Hi Hi Hello Hello world"))
f = open("a.txt","r")
s = f.read()
d = frequency_word(s)

l = []
for i in d:
    l.append(d[i])
s = set(l)
l = list(s)
l.sort(reverse=True)
for i in l:
  for k in d:
    if i == d[k]:
        print(k,i)
