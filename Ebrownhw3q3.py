def convertToBinary(n):
   if n > 1:
       convertToBinary(n//2)
   print(n % 2, end = '')

convertToBinary(23)
print("")
convertToBinary(10)
