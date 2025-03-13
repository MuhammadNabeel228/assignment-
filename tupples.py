# Tuple in python
academic_tuple=('Muhammad Nabeel','Rohail Amin','sp24-bba-091','5.4')
print(academic_tuple)
# single item tuple
Mr_Nabeel_Registration=('sp24-bba-091',)
print(Mr_Nabeel_Registration)
# A tuple of integers
numbers_tuple=(1,4,2,4)
print(numbers_tuple)
# A tuple of strings
string_tuple=('apple','banana','orange')
print(string_tuple)
# A mixed tuple
mixed_tuple=('Ali',1,8.48)
print(mixed_tuple)
# A tuple with a single item
single_item_tuple=(4,)
print(single_item_tuple)
       
# accessing elemets
fruits_tuple=('Mango','Orange','Cherry','Guava','Apple')
print(fruits_tuple[0])
print(fruits_tuple[1])
print(fruits_tuple[-3])
print(fruits_tuple[-2])
# concatenation in tuple
tuple1=(1,2,3,4)
tuple2=(5,6,7,8)
combined_tuple=tuple1+tuple2
print(combined_tuple)
# repitition in tuple
tuple3=('repitition')
repeated_tuple=tuple3*20
print(repeated_tuple)
# slicing a tuple
numbers=(0,1,2,3,4,5,6,7,8,9)
print(numbers[:5])
print(numbers[1:3])
print(numbers[3:])
print(numbers[2:9])
# count a number in tuple
veg_tuple=('carrot','onion','potato','carrot')
print(veg_tuple.count('carrot'))
num_tuple=(3,5,6,3,2,3,4,3)
print(num_tuple.count(3))
fruits_tuple=('Mango','Orange','Cherry','Guava','Apple')
print(fruits_tuple.index('Cherry'))
# break statement in loop
for num in range(1,10):
    if num==5:
        print("Breaking the loop at 5")
        break
    print("Current number:", num)
# continue statement in loop
for num in range(1,10):
    if num==6:
        print("Skipping number 6")
        continue
    print("Current number:", num)
for num in range(1,10):
    if num==5:
        print("Skipping number 5")
        continue
    if num==8:
        print("Breaking the loop at number 8")
        break
    print("Current number:", num)

num = 1
while num<=10:
    if num==5:
        print("Breaking the loop at the number 5")
        break
    print("Current number:", num)
    num+=1

num=0
while num<10:
    num+=1
    if num==5:
        print("Skipping number 5")
        continue
    print("Current number:", num)
    
    

