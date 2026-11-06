"""
loops.py - for loops, while loops and conditions
Module 01: Introduction to AI & Python
"""

# --- for loop with range ---
print("Counting 1 to 5:")
for i in range(1, 6):
    print(i)

# --- Multiplication table using a for loop ---
number = 7
print(f"\nMultiplication table of {number}:")
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

# --- while loop ---
print("\nCountdown:")
count = 5
while count > 0:
    print(count)
    count -= 1
print("Liftoff!")

# --- Loop with if / elif / else ---
print("\nEven or odd for numbers 1 to 6:")
for n in range(1, 7):
    if n % 2 == 0:
        print(n, "is even")
    else:
        print(n, "is odd")

# --- Sum of numbers 1 to 100 ---
total = 0
for n in range(1, 101):
    total += n
print("\nSum of 1 to 100:", total)

# --- break and continue ---
print("\nPrinting numbers, skipping 3 and stopping at 7:")
for n in range(1, 11):
    if n == 3:
        continue   # skip 3
    if n == 7:
        break      # stop the loop at 7
    print(n)
