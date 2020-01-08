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
print(f.read())
