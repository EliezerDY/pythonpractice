n = int(input("Enter anumber:"))
for i in range(n):
  r=1
  for j in range(i):
      r *= 2
  print("2 to power",i,"is",r)
