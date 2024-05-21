#Prompt the user for their email address from the console.
#Write the email address to a file, email.txt.
#Print the email address to the console.
#Write a function that adds/appends a line with your name to the end of the existing email.txt file. Call the function.

emailadd = input("Enter your email address:")
Emailaddress= 'Emailaddress.txt'
with open(Emailaddress) as file_object:
   for line in file_object:
     print(line.rstrip())
with open(Emailaddress, 'a') as file_object:
   file_object.write("Hayley did good on her test..hopfully.\n")
