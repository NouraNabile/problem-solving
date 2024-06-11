# List: ordered,mutable,allows duplicate element
mylist = ["banana","cherry","apple"] # create with value 
print(mylist)

mylist2 = list() # create empty list
print(mylist2)

mylist3 = [5,True,"f3geh"] # with diferen data type
print(mylist3)

mylist4 = [5,True,"f3geh","f3geh"] # duplicate
print(mylist4)

item=mylist4[-2] # most important
print(item)

for i in mylist: #loop
    print(i)

if "banana" in mylist:
    print("yes")
else:
    print("no")    

print(len(mylist)) #lenght

mylist.append("lemon") # appednd/insert detect index
print(mylist)

print(mylist)
mylist.insert(1,"mbjguerhoi")
print(mylist)