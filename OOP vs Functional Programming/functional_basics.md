# Functional Programming (FP) Basics

## What is FP?
Functional Programming (FP) is a programming paradigm that focuses on writing programs using pure functions and immutable data. It avoids changing state and mutable data, ensuring that functions always produce the same output for the same input and have no side effects.

## Key Concepts:
- **Pure Functions:** Functions that produce the same result for the same input and have no side effects.
- **Immutability:** Data cannot be changed after it's created; instead, new data structures are created when changes are needed.
- **Higher-order Functions:** Functions that can take other functions as parameters or return functions as results.

## Example: Pure Function in Python

```python
def square(n):
    return n * n  # Pure function: no side effects

# Calling the function
result = square(4)
print(result)  # Output: 16

No side effects, just input → output.

The square function works solely on its input and always returns the same output for the same input.

Key Takeaways:
Pure Functions make your code predictable and testable.

Immutability leads to safer code by preventing unintended side effects.

Higher-order Functions enable functional composition and flexible code.

This is a fundamental concept in FP that encourages writing clean, modular, and maintainable code!