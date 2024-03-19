#a) Use a list comprehension to generate a list of all even numbers from 0 to 100 inclusive.
evennumbers = [value for value in range (0,101,2)]
print(evennumbers)
#b) Use slicing to print the first five even numbers in the list.
print(evennumbers[0:5])
#c) Use slicing to print the last five even numbers in the list.
print(evennumbers[46:51])
#d) Use slicing to print all list numbers between 20 and 30 inclusive.
print(evennumbers[10:16])