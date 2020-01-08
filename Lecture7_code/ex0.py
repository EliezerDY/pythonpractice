#1
for i in range(1,11):
  print(i)

#2
for i in range(1,101):
  print(i)

#3
for i in range(50,101):
  print(i)

#4
for i in range(1,100):
  if i % 2 == 0:
    print(i)
#4-1
for i in range(2,100,2):
  print(i)

#5
r = 0
for i in range(1,101):
  r += i
print(r)

#6
r = 0
for i in range(1,101):
  if i % 2 == 0:
    r += i
print(r)

#7
r = 0
for i in range(50,101):
  if i % 2 == 0:
    r += i
print(r)

#8
r = 1
for i in range(1,11):
  r *= i
print(r)
