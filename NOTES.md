# Learning Notes: Introduction to AI & Python

**Module 01 | Day 1 – Day 4 | Beginner**

---

## 1. Basics of Artificial Intelligence and Machine Learning

**Artificial Intelligence (AI)** is the field of computer science that builds machines able to do tasks that normally need human intelligence, such as understanding language, recognising images, making decisions and solving problems.

**Machine Learning (ML)** is a part of AI where computers learn patterns from data instead of being given step-by-step rules. The more good data a model sees, the better it usually becomes.

Main types of ML:
- **Supervised learning**: learns from labelled data (e.g. emails marked "spam" or "not spam").
- **Unsupervised learning**: finds hidden patterns in unlabelled data (e.g. grouping customers by behaviour).
- **Reinforcement learning**: learns by trial and error with rewards and penalties (e.g. a game-playing agent).

Typical ML workflow: collect data → clean data → train a model → test it → use it to make predictions.

---

## 2. Difference Between AI, ML and Deep Learning

Think of them as circles inside each other: **AI ⊃ ML ⊃ Deep Learning**.

| | Artificial Intelligence | Machine Learning | Deep Learning |
|---|---|---|---|
| What it is | Broad goal of making machines "smart" | Subset of AI that learns from data | Subset of ML using multi-layer neural networks |
| Data needed | Varies (can be rule-based) | Moderate amounts | Very large amounts |
| Human effort | Rules may be hand-written | Features often chosen by humans | Learns features automatically |
| Example | Chess program with fixed rules | Spam filter | Face recognition, ChatGPT-style models |

---

## 3. Real-World AI Applications

- **Navigation**: Google Maps predicts traffic and suggests the fastest route.
- **Entertainment**: Netflix and YouTube recommend content based on what you watch.
- **Voice assistants**: Siri, Alexa and Google Assistant understand speech.
- **Healthcare**: AI helps detect diseases in X-rays and scans.
- **Banking**: fraud detection spots unusual transactions.
- **E-commerce**: product recommendations and chatbots.
- **Agriculture**: crop disease detection from photos, yield prediction.
- **Self-driving features**: lane detection and obstacle recognition.

---

## 4. Python: Installation and Concepts Practised

### Installing Python
1. Download Python 3 from python.org.
2. During installation, tick **"Add Python to PATH"**.
3. Check it works with `python --version`.
4. Write code in an editor such as VS Code or IDLE.

### Variables and data types
```python
name = "Asha"      # str
age = 20           # int
height = 5.4       # float
is_student = True  # bool
```

### Loops
```python
for i in range(1, 6):
    print(i)

count = 3
while count > 0:
    print(count)
    count -= 1
```

### Functions
```python
def add(a, b):
    return a + b

print(add(5, 7))   # 12
```

### Lists
```python
topics = ["ML", "DL"]
topics.append("NLP")
print(sorted(topics))
print([n ** 2 for n in range(1, 6)])   # [1, 4, 9, 16, 25]
```

---

## 5. Beginner Python Programs I Wrote

- `variables.py`: data types, arithmetic and string operations
- `loops.py`: multiplication table, countdown, sum of 1 to 100
- `functions.py`: greet, add, factorial, average, min/max
- `lists.py`: add, remove, sort, slice, list comprehensions
- `mini_project.py`: a calculator with input validation and history

---

## 6. Problems Faced and How I Solved Them

| Problem | Solution |
|---|---|
| `python` command not recognised | Reinstalled Python and ticked "Add Python to PATH" |
| `IndentationError` | Python needs consistent indentation (4 spaces) inside loops and functions |
| `ValueError` when converting input to a number | Used `try / except` to ask the user again |
| Forgot `:` after `if`, `for`, `def` | Read the error message line number and fixed the syntax |

---

## 7. Key Takeaways

- AI is the big idea, ML is how machines learn from data, and Deep Learning is ML with neural networks.
- Python is popular for AI because its syntax is simple and it has powerful libraries (NumPy, pandas, scikit-learn, TensorFlow, PyTorch).
- Small programs on variables, loops, functions and lists are the foundation for everything that comes next.

**Next step:** learn data handling with NumPy and pandas, then build a simple ML model.
