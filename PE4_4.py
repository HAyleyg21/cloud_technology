#A) Create an empty list named grades.
grades=[]
#B) Add any five grades one at a time to grades.
grades.extend([90,91,92,93,94])
#c) Print the current list.
print('current list:' ,grades)
#d) Compute the total of these grades using the indexing to reference each number in grades.
total_grades = grades[0] +grades[1] +grades[2] +grades[3] +grades[4]
print(total_grades)
#e) Compute the average of these grades using the len () function.
avg_grades = total_grades / len(grades)
print(avg_grades)
#f) Print the average with a precision of two decimal places.
#g) Use two different methods to remove all failing grades (lower than 60) one at a time from the list.
grades.remove(90)
grades.remove(91)
#h) Print the updated list.
print('updated list:' ,grades)
#I
avg_grades = sum(grades)/ len(grades)
print  ('avg_grades:' ,round(avg_grades,3))