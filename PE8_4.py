#A) Create a dictionary, stuInfo with the keys name, gpa, and age. Give appropriate values for each key.
stuInfo = {'Name': 'janet' , "GPA": 3.5, 'age': 19}
#b) Use a loop and the items() method to print all keys and values.\
for key, value in stuInfo.items():
    print(key + ":" , value)
#c) Use the update() method to change the gpa to 4.0.
    stuInfo.update({'GPA': 4.0})
#d) Use a loop and the keys() method to print all keys and values.
    print("/n")
    for key in stuInfo.keys():
        print(key + ":" , stuInfo[key])
#e) Add a key major with the value to the dictionary.
        stuInfo['major'] = 'Computer Science'
#f) Use a loop and the values() method to print all values.
    print("/n")
    for value in stuInfo.values():
            print(value)
#g) Use two different ways to delete gpa and age in the dictionary.
            stuInfo.pop('GPA')
            stuInfo.pop('age')
#h) Print the updated dictionary.
            print("/n")
            print(stuInfo)
