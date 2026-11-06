"""
functions.py - Defining and using functions
Module 01: Introduction to AI & Python
"""


def greet(name):
    """Print a greeting for the given name."""
    print(f"Hello, {name}! Welcome to AI & Python.")


def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def area_of_circle(radius, pi=3.14159):
    """Return the area of a circle. 'pi' has a default value."""
    return pi * radius ** 2


def is_even(number):
    """Return True if the number is even, otherwise False."""
    return number % 2 == 0


def factorial(n):
    """Return n! calculated with a loop."""
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def average(numbers):
    """Return the average of a list of numbers."""
    return sum(numbers) / len(numbers)


def min_max(numbers):
    """Return both the smallest and largest numbers (two return values)."""
    return min(numbers), max(numbers)


# --- Calling the functions ---
greet("Asha")
print("add(5, 7) =", add(5, 7))
print("Area of circle with radius 3 =", round(area_of_circle(3), 2))
print("Is 10 even?", is_even(10))
print("Is 7 even?", is_even(7))
print("5! =", factorial(5))

marks = [78, 85, 92, 66, 89]
print("Average marks:", average(marks))

smallest, largest = min_max(marks)
print("Smallest:", smallest, "| Largest:", largest)
