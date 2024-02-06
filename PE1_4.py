price = 99.99 #a
discountpercent = 25 #b 
markdown = (discountpercent /100) * price #c 
newprice = price - markdown #d 
print ("price =", round ( newprice, 2) ) #e