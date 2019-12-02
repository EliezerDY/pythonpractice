a = input("Enter a word ('stop' to end program): ")
sentence = " "
while a != ("stop"):
    sentence = sentence + " " +  a
    a = input("Enter a word ('stop' to end program): ")
r = ' '.join(reversed(sentence.split(' ')))
print(r)
