# Converting two lists into one dictionary:
keys = {'Ten' , 'Twenty' , 'Thirty'}
values = [10, 20, 30]
result = {keys: values for keys, values in zip (keys, values)}
print(result)