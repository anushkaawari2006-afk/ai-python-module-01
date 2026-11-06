"""
variables.py - Variables and data types in Python
Module 01: Introduction to AI & Python
"""

# --- Basic data types ---
name = "Asha"          # str  (text)
age = 20               # int  (whole number)
height = 5.4           # float (decimal number)
is_student = True      # bool (True / False)

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is student:", is_student)

# --- Checking the type of a variable ---
print("\nTypes:")
print(type(name), type(age), type(height), type(is_student))

# --- Arithmetic ---
a = 15
b = 4
print("\nArithmetic with a = 15 and b = 4:")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor division:", a // b)
print("Remainder (modulus):", a % b)
print("Power:", a ** b)

# --- String operations ---
language = "Python"
print("\nString operations:")
print("Upper:", language.upper())
print("Lower:", language.lower())
print("Length:", len(language))
print("First letter:", language[0])
print("Greeting:", f"I am learning {language} for AI!")

# --- Type conversion ---
number_text = "100"
number = int(number_text) + 50
print("\nConverted '100' to int and added 50:", number)

# --- Taking input (uncomment to try it) ---
# user_name = input("Enter your name: ")
# print("Hello,", user_name)
