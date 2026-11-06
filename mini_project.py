"""
mini_project.py - Simple Calculator (beginner project)
Module 01: Introduction to AI & Python

Uses variables, loops, functions and lists together.
"""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: cannot divide by zero"
    return a / b


def get_number(prompt):
    """Keep asking until the user enters a valid number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def main():
    history = []  # list that stores past calculations

    print("=== Simple Calculator ===")
    while True:
        print("\n1. Add  2. Subtract  3. Multiply  4. Divide  5. History  6. Quit")
        choice = input("Choose an option (1-6): ").strip()

        if choice == "6":
            print("Goodbye!")
            break

        if choice == "5":
            if not history:
                print("No calculations yet.")
            for item in history:
                print(item)
            continue

        if choice not in ("1", "2", "3", "4"):
            print("Invalid choice, try again.")
            continue

        x = get_number("Enter first number: ")
        y = get_number("Enter second number: ")

        if choice == "1":
            result, symbol = add(x, y), "+"
        elif choice == "2":
            result, symbol = subtract(x, y), "-"
        elif choice == "3":
            result, symbol = multiply(x, y), "*"
        else:
            result, symbol = divide(x, y), "/"

        line = f"{x} {symbol} {y} = {result}"
        print("Result:", line)
        history.append(line)


if __name__ == "__main__":
    main()
