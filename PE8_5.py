#a) Create a dictionary, rank = {1:"Freshman", 2:"Sophmore", 3:"Junior", 4:"Senior"}
rank = {1:"Freshman", 2:"Sophmore", 3:"Junior", 4:"Senior"}
#b) Request a user input for a number of years.
years = int(input("Enter a number of years (1-4):"))
#c) Print the value of the matching key in the dictionary.
if years in rank :
    print("you are a" , rank[years])
else:
    print("Invaild input. Please enter a number between 1 and 4")
#d) Print the error message if input is invalid.
    print("Invaild years, Please enter a vaild number")