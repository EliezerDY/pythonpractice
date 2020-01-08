min = int(input("Enter a min:"))
max = int(input("Enter a max:"))
if max > min:
  for i in range(max-1,min,-1):
    if i%2 != 0:
        print(i)
else:
  print(max,"is less than",min,"invalid")
