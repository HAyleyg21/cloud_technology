#A) Create a list below and print it out.
months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november',
'december']
#B Use a for loop to store each month with its first three-letter abbreviation into a new list.
abbreviations = [months[:3] for months in months]
print(abbreviations)
#c Print the value of each month in uppercase separated by a ‘|’ in a row as displayed in the example output.
print('l' . join (abbreviations.upper()for abbreviations in abbreviations))
#d Print the new list.
print("/Newlist:")
print(abbreviations)
