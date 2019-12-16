import random

lotteryNumbers = []
NumList = []

print("Lottery Game")
print(" ")
for i in range(6):
    value = int(input("Please enter the Value of Pick %d from 0-59 (new value): " %i))
    NumList.append(value)

for i in range (0,6):
  number = random.randint(1,59)
  while number in lotteryNumbers:

    number = random.randint(1,59)


  lotteryNumbers.append(number)


lotteryNumbers.sort()

print("Your numbers:", NumList)
print("Today's lottery numbers are: ")
print(lotteryNumbers)

if NumList == lotteryNumbers:
    print("You won a MILLION DOLLARS!!")
    print("Your total return is $980925.00")

match = any(check in NumList for check in lotteryNumbers)
if match:
    print("You win 1000")
    print("Your total loss is $8000")
else :
    print("Play again")
