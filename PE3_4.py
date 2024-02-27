#a) Prompt and request three integer numbers one by one from the console.
#b) Sort these numbers and print them from smallest to largest.
number1 = int(input("Please enter the first integer: "))
number2 = int(input("Please enter the first integer: "))
number3 = int(input("Please enter the first integer: "))

sorted_numbers = sorted( {number1,number2,number3})
print("Before Sorting: {number1} {number2} {number3}")
print("After Sorting:{' 'join(map(str, sorted_numbers))} ")

print("""" 
      Before Sorting: 7,8,1
      After Sorting: 1,7,8""")

