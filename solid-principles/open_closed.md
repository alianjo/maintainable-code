# Open/Closed Principle (OCP)

## Explanation  
The **Open/Closed Principle (OCP)** states that a class should be **open for extension but closed for modification**.  
This means we should be able to **add new functionality** without changing the existing code.

---

## Bad Example – Violating OCP:
```python
class Discount:
    def calculate(self, price, discount_type):
        if discount_type == "percentage":
            return price * 0.9
        elif discount_type == "fixed":
            return price - 10
Problem:
Every time we need a new discount type, we have to modify the class, breaking OCP.

Good Example – Applying OCP:
from abc import ABC, abstractmethod

class Discount(ABC):
    @abstractmethod
    def apply(self, price):
        pass

class PercentageDiscount(Discount):
    def apply(self, price):
        return price * 0.9

class FixedDiscount(Discount):
    def apply(self, price):
        return price - 10
Why is this better?
✔ We can add new discount types without modifying existing code.
✔ The system is scalable and maintainable.