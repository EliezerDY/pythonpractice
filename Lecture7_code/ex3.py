n = input("Enter anumber:")
a = int(n)
for i in range(len(n)):
  print(a%10)
  a = a//10
