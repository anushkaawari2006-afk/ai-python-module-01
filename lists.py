"""
lists.py - Working with lists
Module 01: Introduction to AI & Python
"""

# --- Creating a list ---
ai_topics = ["Machine Learning", "Deep Learning", "NLP"]
print("Start:", ai_topics)

# --- Adding items ---
ai_topics.append("Computer Vision")
ai_topics.insert(1, "Neural Networks")
print("After adding:", ai_topics)

# --- Removing items ---
ai_topics.remove("NLP")
last = ai_topics.pop()
print("Removed 'NLP' and popped:", last)
print("After removing:", ai_topics)

# --- Indexing and slicing ---
print("\nFirst item:", ai_topics[0])
print("Last item:", ai_topics[-1])
print("First two items:", ai_topics[:2])

# --- Sorting ---
numbers = [42, 7, 19, 3, 25]
print("\nOriginal numbers:", numbers)
print("Sorted ascending:", sorted(numbers))
print("Sorted descending:", sorted(numbers, reverse=True))

# --- Useful built-in functions ---
print("\nLength:", len(numbers))
print("Sum:", sum(numbers))
print("Min:", min(numbers), "| Max:", max(numbers))

# --- Looping through a list ---
print("\nLooping through the list:")
for index, topic in enumerate(ai_topics, start=1):
    print(f"{index}. {topic}")

# --- Checking membership ---
print("\nIs 'Deep Learning' in the list?", "Deep Learning" in ai_topics)

# --- List comprehension (squares of numbers) ---
squares = [n ** 2 for n in range(1, 8)]
print("\nSquares of 1 to 7:", squares)

# --- Even numbers only ---
evens = [n for n in range(1, 21) if n % 2 == 0]
print("Even numbers up to 20:", evens)
