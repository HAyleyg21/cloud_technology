#a) Create three stuInfo dictionaries with the keys: name and value: gpa. Add appropriate values for each key.
studentinfo1= {'name': 'Lisa', 'GPA': 2.5}
studentinfo2= {'name': 'Hayley', 'GPA': 4.0}
studentinfo3= {'name': 'Tia', 'GPA': 1.7}
#b) Create a list stuClass, add all dictionaries to this list, and print the list.
stuClass = [studentinfo1, studentinfo2, studentinfo3]
print("List of students in stuClass:" , stuClass)
#c) Use a loop to print all students from the list of stuClass.
print("/n all students instructclass")
for students in stuClass:
    print(students)
#d) Use a loop to print all the gpa.
print("/n All Gpa information:")
for students in stuClass:
   print(students['GPA'])
#e) Change the last student’s gpa to 4.0.
   stuClass[-1] ['GPA'] = 4.0
#f) Add a new student info to the list.
newstudent ={'NAME': 'TALLY', 'GPA': 4.0}
stuClass.append(newstudent)
#g) Use a loop to print all the names and gpa with proper format as the output below
print("/n All updated information")
for students in stuClass:
    print("Name:" , students['name']), [students['GPA']]