#a) Prompt and request input the amount of the bill (in float) and the percentage of tip (in integer). 
#b) Calculate, set the result to two decimal places and print the result.
bill = float(input("Enter the amount of the bill: $"))
tip = int(input("Enter the tip percentage:  "))
amount = (tip/100) * bill
print(amount)

