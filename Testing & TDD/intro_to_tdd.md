# Introduction to Test-Driven Development (TDD)

## 🛠 What is TDD?
**Test-Driven Development (TDD)** is a **software development process** that relies on **writing tests before writing the actual implementation**. It follows a structured cycle:

1. **Write a test** (which initially fails).
2. **Implement the code** to pass the test.
3. **Refactor** the code while keeping the test passing.

---

## The TDD Cycle
The TDD workflow follows these **three steps** repeatedly:

1️. **Red** → Write a failing test.  
2. **Green** → Write just enough code to make the test pass.  
3️. **Refactor** → Improve the code while keeping all tests passing.  

---

## Example – Applying TDD:

### Step 1: Write a Failing Test (Red)
```python
def test_add():
    assert add(2, 3) == 5  # This will fail because 'add' is not implemented yet
Step 2: Write Just Enough Code to Pass (Green)

def add(a, b):
    return a + b

Step 3: Refactor (if needed)

# No refactoring needed in this simple case
Why Use TDD?
✔ Ensures better code quality
✔ Reduces debugging time
✔ **Encourages writing modular & test