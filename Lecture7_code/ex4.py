n = int(input("Enter anumber:"))
for i in range(1,n+1):
  r=1
  for j in range(1,i+1):
      r *= j
  print(i,"! = ",r)
