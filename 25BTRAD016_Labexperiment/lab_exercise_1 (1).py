# NAME: Harnish B
# USN: 25BTRAD016
# Python Lab Exercises - Tasks 1 to 18

# Task 1 - Print Name, Department, College
print("Task 1")
print("Name: Harnish B")
print("Department: Computer Science Engineering")
print("College: Jain University")

# Task 2 - Print Pattern
print("\nTask 2")
print("*******")
print("*******")
print("*******")

# Task 3 - Single print() statement
print("\nTask 3")
print("Python is Easy")

# Task 4 - Number Pattern
print("\nTask 4")
print("1")
print("12")
print("123")
print("1234")
print("12345")

# Task 5 - Using \n
print("\nTask 5")
print("Computer\nScience\nEngineering")

# Task 6 - Using \t
print("\nTask 6")
print("Name\tAge\tCity")

# Task 7 - Single-line comment
print("\nTask 7")
# This program prints a welcome message
print("Welcome to Python")

# Task 8 - Multi-line comments
print("\nTask 8")
"""
This is a multi-line comment.
This program demonstrates
the use of comments in Python.
"""
print("Python Programming")

# Task 9 - Three comments and three print statements
print("\nTask 9")
# First print statement
print("Hello")
# Second print statement
print("Welcome to Python")
# Third print statement
print("Programming is Easy")

# Task 10 - Create a variable called name
print("\nTask 10")
name = "Harnish B"
print(name)

# Task 11 - Store 10, 20, 30 in three variables
print("\nTask 11")
a = 10
b = 20
c = 30
print(a)
print(b)
print(c)

# Task 12 - Convert string "100" into an integer value
print("\nTask 12")
value = "100"
number = int(value)
print("Value:", number)
print("Data type:", type(number))

# Task 13 - Convert integer 25 into a float
print("\nTask 13")
number = 25
value = float(number)
print("Value:", value)
print("Data type:", type(value))

# Task 14 - Accept user's age
print("\nTask 14")
age = int(input("Enter your age: "))
print("Your age is:", age)

# Task 15 - Accept two numbers and display their sum
print("\nTask 15")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
total = num1 + num2
print("Sum:", total)

# Task 16 - Using f-string
print("\nTask 16")
name = input("Enter your name: ")
age = int(input("Enter your age: "))
cgpa = float(input("Enter your CGPA: "))
print(f"My name is {name}. I am {age} years old and my CGPA is {cgpa}.")

# Task 17 - Celsius to Fahrenheit
print("\nTask 17")
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32
print(f"Temperature in Fahrenheit: {fahrenheit:.2f}")

# Task 18 - Even or Odd
print("\nTask 18")
number = int(input("Enter number: "))
if number % 2 == 0:
    print(f"{number} is Even")
else:
    print(f"{number} is Odd")
