#A
fruits = ["apple", "banana", "cherry"]
for item in fruits:
  print(item)

#B
for i in range (1, 4):
    print(i,'\t' , 2**i)

#C Why is there no output when you run the code?
for j in range (1, 6, -1):
 print(j)

#D How to display all the elements in uppercase?
letters = ['a', 'b', 'c']
for letter in letters:
  letter = letter.upper()
print(letters)

#E
fruits = ('apple', 'banana', 'cherry')
print(fruits)
fruits = ['orange']
fruits.append ('pineapple')
print(fruits)
