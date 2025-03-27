# sorted a list

mylist1=[]
print("enter objects of first list")
for i in range(5):
    value=input("enter a value:")
    n=int(value)
    mylist1.append(n)

mylist2=[]
print("enter objects of second list")
for i in range(5):
    value=input("enter a value:")
    n=int(value)
    mylist2.append(n)

mylist3=mylist1+mylist2
mylist3.sort()
print(mylist3)

# find largest and smallest element in list

mylist=[]
print("enter objects of first list")
for i in range(5):
    value=input("enter a value:")
    n=int(value)
    mylist.append(n)

print(mylist)
print("maximum value of list is:",max(mylist))
print("minimum value of list is:",min(mylist))

#find the smallest and largest index value

mylist=[]
print("enter objects of list")
for i in range (5):
    value=input("enter a value:")
    n=int(value)
    mylist.append(n)

print(mylist)
print(mylist.index(max(mylist)))

# list in descending order

mylist=[]
print("enter objects of list")
for i in range(10):
    value=input("enter a value:")
    n=int(value)
    mylist.append(n)
print(mylist)
mylist.sort()
print(mylist)
mylist.reverse()
print(mylist)
