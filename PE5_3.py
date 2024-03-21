#a) Create a list comprehension of multiples of 4 from 0 to 10 inclusive.
multiples = [value *4 for value in range(11)]
#b) Print this list as displayed in the example output.
print (multiples)
#c) Create a second empty list.
multiple = []
#D) Use a loop to insert all elements from the first list to the second list.
for value in multiples:
    multiple.append(value//2)
#e) Print the second list as displayed in the example output.
    print(multiple)
#f) Use slicing to copy the second list to a new third list.
    third =  multiple [:]
#g) Use a loop to divide and store each element of the third list by 2.
for x in range (len(third)):
    third[x]/=2
#h) Print the third list as displayed in the example output.
print(third)