# for multi lines use three quotation marks
a = """g s dhd
 dhdhh """
print(a)
# start index value from 0
#can print -# such as a([-4])
#slicing first included, last excluded
s = "fruit"
print(s[:])
print(len(a))
b = "  Hello world   "
print(b.strip())
c = "HELLO WORLD"
print(c.lower())
print(b.upper())
print(s.replace("f","b"))
print(a.find("g"))
# in operator =membership operator will print true or not if in
print("g" in a)
# string contenation
a = "Hello"
b ="World"
c =a + b
print(c)
#format method
txt = "My name is Bob and I'm {}"
print(txt.format("10"))
#string comparision follows order of a b c's
print("banana" > "tomato")
print("banana" > "banana")
print("banana" > "banama")
