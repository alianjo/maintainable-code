# Maintainable Code Repository

This repo is a collaborative space to learn and discuss best practices for writing maintainable, readable, and scalable code.

## 📌 Topics Covered
- **SOLID Principles**
- **Clean Code**
- **Testing & TDD**
- **Object-Oriented Programming (OOP) & Functional Programming**
- More to be added by contributors! 🚀

## How to Contribute
1. **Fork** this repository.
2. Create a new branch: `git checkout -b feature-topic-name`.
3. Add your content.
4. Commit your changes: `git commit -m "Added topic XYZ"`.
5. Push to your branch: `git push origin feature-topic-name`.
6. Open a **Pull Request**!

## Discussions & Learning
Feel free to open issues for discussions, ask questions, or suggest new topics!

Let's make this a great resource together! 🎯

## SOLID Principles

### 1. Single Responsibility Principle (SRP)
A class should have only one reason to change, meaning it should have only one job.

#### Example:
```python
class Invoice:
    def __init__(self, items, customer):
        self.items = items
        self.customer = customer
    
    def calculate_total(self):
        return sum(item.price for item in self.items)
```

The `Invoice` class handles only invoice-related logic and does not manage printing or storing invoices.

---
### 2. Open/Closed Principle (OCP)
Software entities should be open for extension but closed for modification.

#### Example:
```python
class Discount:
    def apply_discount(self, total):
        return total

class SeasonalDiscount(Discount):
    def apply_discount(self, total):
        return total * 0.9  # 10% discount
```

New discount types can be added without modifying existing code.

---
### 3. Liskov Substitution Principle (LSP)
Subtypes must be substitutable for their base types without affecting correctness.

#### Example:
```python
class Bird:
    def fly(self):
        pass

class Sparrow(Bird):
    def fly(self):
        print("Sparrow is flying")
```

A `Sparrow` can replace `Bird` without breaking the functionality.

---
### 4. Interface Segregation Principle (ISP)
Clients should not be forced to depend on interfaces they do not use.

#### Example:
```python
class Printer:
    def print(self):
        pass

class Scanner:
    def scan(self):
        pass
```

Instead of one large interface, separate interfaces are created based on functionality.

---
### 5. Dependency Inversion Principle (DIP)
High-level modules should not depend on low-level modules. Both should depend on abstractions.

#### Example:
```python
class EmailService:
    def send_email(self, message):
        pass

class Notification:
    def __init__(self, service: EmailService):
        self.service = service
```

The `Notification` class depends on the abstraction `EmailService`, not a concrete class.

---
## Clean Code

### Writing Readable Code
- Use meaningful variable names
- Keep functions small and focused
- Avoid deep nesting
- Use comments wisely

#### Example:
```python
def calculate_area(radius):
    """Returns the area of a circle given the radius."""
    return 3.14 * radius * radius
```

The function name and docstring explain its purpose clearly.

---
## Testing & TDD

### Why Testing is Important
- Prevents bugs
- Improves code quality
- Provides confidence when refactoring

### What is TDD?
Test-Driven Development (TDD) is a cycle of writing tests before writing actual code.

#### TDD Process:
1. Write a failing test.
2. Write the minimum code to pass the test.
3. Refactor the code while ensuring tests still pass.

#### Example:
```python
import unittest

def add(a, b):
    return a + b

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

if __name__ == "__main__":
    unittest.main()
```

---
## OOP vs Functional Programming

### Object-Oriented Programming (OOP)
- Uses classes and objects
- Encapsulates data and behavior
- Follows principles like inheritance and polymorphism

#### Example:
```python
class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year

    def drive(self):
        print(f"Driving {self.model}")
```

---
### Functional Programming
- Uses pure functions
- Avoids changing state
- Uses higher-order functions and recursion

#### Example:
```python
def square(n):
    return n * n

numbers = [1, 2, 3, 4]
squared_numbers = list(map(square, numbers))
```
