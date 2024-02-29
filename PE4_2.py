#a) Create an empty list called n.
n=[]
#b) Add 2 and 4 into the list.
n.extend([2,4])
#c) Print the list.
print(n)
#d) Add 0, 1 and 3 in proper order.
n.insert(0, 0 )
n.insert(1,1)
n.insert(3,3)
#e) Print the list
print(n)
#f) Add 5 in proper order
n.insert(5,5)
#g)Print the list
print(n)
#h)Remove 0 from the list.
n.remove(0)
#i) Print the list.
print(n)
#j)Remove and print 2 from the list.
rev1 = (n.pop(1))
print (rev1)
#k)Print the list.
print(n)
#l)Remove and print 4 from the list.
rev2=(n.pop(2))
print (rev2)
#m) Print the list.
print(n)
#n)Add all the removed numbers and print the sum.
sum_removed = rev1 + rev2
#o) Change the first item to 100 and last item to 9.9.
n.insert(0,100)
n.insert(4,99)
print(n)
#p) Copy the list n to a newNum list.
newlist=list(n)
print("newlist:", newlist)
#q) Clear the list n.
n.clear()
#r) Print the original list, n and the newNum list.
print(n)
#s) Delete the list n.
del n [:]