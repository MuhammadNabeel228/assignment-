num = float(input("Enter a number:"))
Enter number:2
>>> if num >0:
	print ("Positive")
elif num <0:
	print ("Negative")
else:
	print ("Zero")

	
Positive
>>> year = int(input("Enter a year"))
Enter a year2020
>>> if (year%400 == 0) or (year%4 == 0 and year%100!= 0):
	print("Leap year")
else:
	print("Not a leap year")

	
Leap year
marks = float(input("Enter student marks:"))
if marks >= 85:
    grade = 'A'
elif marks >=70:
    grade = 'B'
elif marks >= 50:
    grade = 'C'
else:
    grade = 'F'
print (f"Grade:{grade}")
 num1 = float(input("Enter first number:"))
Enter first number:2
>>> num2 = (input("Enter second number:"))
Enter second number:5
>>> if op == '+':
	result = num1 + num2
elif op == '-':
	result = num1 - num2
elif op == '*':
	result = num1 * num2
elif op == '/':
    if num2 == 0:
        print("Error: Division by zero!")
        exit()
    result = num1 / num2
else:
    print("Invalid operator")
    exit()

print(f"Result:{result}")

          
