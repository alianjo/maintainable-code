### **Object-Oriented Programming (OOP) Basics**

#### What is OOP?
Object-Oriented Programming (OOP) is a programming paradigm that organizes code into objects. It emphasizes **encapsulation, inheritance, polymorphism,** and **abstraction** to create modular and reusable code.

#### Encapsulation:
Encapsulation is the practice of keeping an object's internal state private while exposing only necessary functionalities through public methods. This helps in organizing and protecting data.

---

### **Example: Encapsulation in Python**
```python
class Car:
    def __init__(self, model):
        self.model = model  # Public attribute
        self.__speed = 0  # Private attribute (denoted by '__')

    def drive(self):
        self.__speed = 60  # Internal state change
        return f"{self.model} is driving at {self.__speed} km/h"

    def get_speed(self):
        return self.__speed  # Accessing private attribute via a method

# Creating an object
my_car = Car("Tesla Model 3")
print(my_car.drive())
print("Current speed:", my_car.get_speed())
```
---

### 🔹 Key Takeaways:
**Encapsulation** keeps data secure and structured.
**Objects** are instances of classes containing attributes and methods.
**Public & Private Attributes** control access to data.

This is a fundamental concept in OOP that ensures better maintainability and security in code! 