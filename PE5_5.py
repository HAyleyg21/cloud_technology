#a) Request an integer input range.
rangeend = int(input("Enter the range end for the multiplication table:"))
#b) Implement a list of the numbers 1 to range inclusive.
number = list(range(1, rangeend +1))
#c) Request an integer input number.
multiplicationnumbers = int(input("Enter the number for which you want the multiplication table:"))
print(f" multiplication table of (multiplicationnumbers):")
#d) Use a loop upon this list to compute and print the multiplication table of the input number.
for num in number:
    print(f"{multiplicationnumbers} {num} = {multiplicationnumbers * num}")