# maintainable-code

This project demonstrates various programming principles that promote maintainability, readability, and scalability of software. The main principles covered in this project include **Clean Code**, **SOLID Principles**, **Test-Driven Development (TDD)**, and more.

## Contents
- [Clean Code Principles](#clean-code-principles)
  - [Code Structure](clean-code-principles/code_structure.md)
  - [Code Comments and Documentation](clean-code-principles/comments_and_docstrings.md)
  - [Naming Conventions](clean-code-principles/naming_conventions.md)
- [Object-Oriented Programming vs Functional Programming](#object-oriented-programming-vs-functional-programming)
  - [Functional Programming Basics](OOP%20vs%20Functional%20Programming/functional_basics.md)
  - [Object-Oriented Programming Basics](OOP%20vs%20Functional%20Programming/oop_basics.md)
  - [OOP vs FP Comparison](OOP%20vs%20Functional%20Programming/oop_vs_fp_comparison.md)
- [SOLID Principles](#solid-principles)
  - [Single Responsibility Principle (SRP)](solid-principles/single_responsibility.md)
  - [Open/Closed Principle (OCP)](solid-principles/open_closed.md)
  - [Liskov Substitution Principle (LSP)](solid-principles/liskov_substitution.md)
  - [Interface Segregation Principle (ISP)](solid-principles/interface_segregation.md)
  - [Dependency Inversion Principle (DIP)](solid-principles/dependency_inversion.md)
- [Testing & TDD](#testing-and-tdd)
  - [Introduction to TDD](testing-and-tdd/intro_to_tdd.md)
  - [Why Testing is Important](testing-and-tdd/why_testing_matters.md)
- [Project Example: Python Project Structure](#project-example-python-project-structure)

## Clean Code Principles

Clean code is a set of practices and principles that ensure software is easy to read, maintain, and extend. Following these principles helps developers collaborate more effectively and reduce technical debt.

## Code Structure

### 1. **File Organization:**
- **Modularity:** Break down your code into multiple files and modules based on functionality.
- **Naming Conventions:** Use consistent and descriptive naming conventions for files and directories.

### 2. **Functions and Methods:**
- **Single Responsibility Principle:** Each function should perform a single task.
- **Descriptive Names:** Use meaningful names instead of generic ones like `doSomething`.

### 3. **Classes and Objects:**
- **Encapsulation:** Group related properties and methods inside classes.
- **Inheritance and Polymorphism:** Reduce redundancy by structuring your classes properly.

### 4. **Consistent Formatting:**
- **Indentation:** Use consistent indentation (2 or 4 spaces per level).
- **Spacing and Line Breaks:** Visually separate different sections of the code.

## Code Comments and Documentation

### 1. **Inline Comments:**
Use comments to explain complex logic:
```python
# Multiply price by quantity to get the total
def calculate_total(price, quantity):
    return price * quantity
```

### 2. **Function and Method Documentation:**
Provide docstrings for better understanding:
```python
def calculate_total(price, quantity):
    """
    Calculate the total price based on price and quantity.
    
    Parameters:
    price (float): The price of one item.
    quantity (int): The number of items.
    
    Returns:
    float: The total price.
    """
    return price * quantity
```

### 3. **Class Documentation:**
```python
class User:
    """
    Represents a user in the system.
    
    Attributes:
    username (str): The username of the user.
    email (str): The email address of the user.
    """
    def __init__(self, username, email):
        self.username = username
        self.email = email
```

## Naming Conventions

### 1. **Variables:**
Use snake_case for variables in Python.
```python
total_price = 100
user_age = 25
```

### 2. **Functions:**
```python
def calculate_total_price(price, quantity):
    return price * quantity
```

### 3. **Classes:**
Use PascalCase for class names.
```python
class User:
    pass
```

### 4. **Constants:**
Use ALL_CAPS for constants.
```python
MAX_USERS = 100
```

## Project Example: Python Project Structure
A well-structured Python project typically includes directories for source code, tests, and documentation. Here's an example of how to organize your project files:

```
my_project/
│
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── utils.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── order.py
│   └── controllers/
│       ├── __init__.py
│       ├── user_controller.py
│       └── order_controller.py
│
├── tests/
│   ├── __init__.py
│   ├── test_main.py
│   ├── test_utils.py
│   └── test_models/
│       ├── __init__.py
│       ├── test_user.py
│       └── test_order.py
│
└── README.md
```

### Key Points:
- **`src/`**: Contains the source code of the project.
- **`tests/`**: Contains test files.
- **`README.md`**: Provides an overview of the project.
By following these principles and practices, you can create a well-structured codebase that is easy to read, maintain, and scale.
