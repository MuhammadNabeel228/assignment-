Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:44:40) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> num = float(input("Enter a number:"))
Enter a number:2
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
>>> num1 = float(input("Enter first number:"))
Enter first number:2.o
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    num1 = float(input("Enter first number:"))
ValueError: could not convert string to float: '2.o'
>>> num1 = float(input("Enter first number:"))
Enter first number:2
>>> num2 = float(input("Enter second number:"))
Enter second number:5
>>> if op == '+'
SyntaxError: invalid syntax
>>> num1 = float(input("Enter first number:"))
Enter first number:2
>>> num2 = float(input("Enter second number:"))
Enter second number:5
SyntaxError: multiple statements found while compiling a single statement
>>> num1 = float(input("Enter first number:"))
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
	ifnum2 == 0:
		
SyntaxError: invalid syntax
>>> num1 = float(input("Enter first number:"))
Enter first number:2
>>> num2 = (input("Enter second number:"))
Enter second number:5
>>>  if op == '+':
	 
SyntaxError: unexpected indent
>>> num1 = float(input("Enter first number:"))
Enter first number:2
>>>  num2 = (input("Enter second number:"))
 
SyntaxError: unexpected indent
>>> num1 = float(input("Enter first number:"))
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
	result = num / num2

	
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    if op == '+':
NameError: name 'op' is not defined
>>> marks = float(input("Enter student marks:"))
Enter student marks:75
>>> if marks >= 85:
	grade = 'A'
elif marks >= 70:
	grade = 'B'
elif marks >= 50:
	grade = 'C'
else:
	grade = 'F'
	print(f"Grade:{gade}")
	
SyntaxError: invalid syntax
>>> marks = float(input("Enter student marks:"))
Enter student marks:75
>>> if marks >= 85:
	grade = 'A'
elif marks >= 70:
	grade = 'B'
elif marks >= 50:
	grade = 'C'
else:
	grade = 'F'
	
SyntaxError: multiple statements found while compiling a single statement
>>> marks = float(input("Enter student marks:"))
Enter student marks:75
>>> if marks >= 85:
	grade = 'A'
elif marks >= 70:
	grade 'B'
	
SyntaxError: invalid syntax
>>> marks = float(input("Enter student marks:"))
Enter student marks:75
>>> if marks >=85:
	grade = 'A'
elif marks >=70:
	grade = 'B'
elif marks >= 50:
	grade = 'C'
else:
	grade = 'F'
print(f"Grade:{grade}")
SyntaxError: invalid syntax
>>> marks = float(input("Enter student marks:"))
Enter student marks:75
>>> if marks >=85:
	print(grade = 'A')

	
>>> 
>>> marks = float(input("Enter student marks:"))
Enter student marks:75
>>> if marks >= 85:
	print(grade = 'A')
elif marks >=70:
	print(grade = 'B')
elif marks >= 50:
	print(grade = 'C')
else:
	print(grade = 'F')

	
Traceback (most recent call last):
  File "<pyshell#88>", line 4, in <module>
    print(grade = 'B')
TypeError: 'grade' is an invalid keyword argument for this function
>>> marks=float(input("Enter student marks:"))
Enter student marks:75
>>> if marks>=85:
	print("Grade: A")
elif marks>=70:
	print("Grade: B")
elif marks>=50:
	print("Grade: C")
else:
	print("Grade: F")

	
Grade: B
>>> 
