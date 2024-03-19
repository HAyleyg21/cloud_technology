#A
fruits = ["apple", "pear", 'python',]
for item in fruits:
    print(f"{item.title()} is my favorite!") 
    print(f"I want to have more {item}.\n")

#B
numbers = [1,2,3,4,5]
for n in numbers:
    print(n)
print("Thats all the numbers in the list.")
print("numbers = ", numbers)

#C
n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
count = 0
for i in n:
    print(i, end = '\t')
count += 1
print(f"\nThere are {count} numbers in the list.")
print("n = ", n)

#D
languages = ["c++", "java", "python"]
for code in languages:
 print(code.upper(), end = " | ")
else:
    print("Enjoy coding!")

#E
n = -6, 7, 3, -2, 6, 3, 9
print(len(n), max(n), min(n), sum(n), sep = '\n')
print(n.count(3), n.index(3), n[-6:6], sep = '\n')
print(n, sorted(n), sep = '\n')

#F
a = 2
b = 3
print(type(a+b))
print(type((a+b,)))
print(type(())) 
