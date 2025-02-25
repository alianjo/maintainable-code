# Interface Segregation Principle (ISP)

## Explanation  
The **Interface Segregation Principle (ISP)** states that **a class should not be forced to implement interfaces it does not use**. Instead of having **large, monolithic interfaces**, we should create **smaller, more specific ones**.

---

## Bad Example – Violating ISP:
```python
from abc import ABC, abstractmethod

# Large interface with unrelated methods
class Worker(ABC):
    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def eat(self):
        pass

# A robot can work but cannot eat!
class Robot(Worker):
    def work(self):
        return "Robot is working"

    def eat(self):
        raise Exception("Robots don't eat!")
Problem:

Robot is forced to implement eat(), even though it does not need it.
Violates ISP by creating an interface that is too broad.
Good Example – Applying ISP:

from abc import ABC, abstractmethod

# Separate interfaces for different responsibilities
class Workable(ABC):
    @abstractmethod
    def work(self):
        pass

class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass

# A human needs both work & eat functionalities
class Human(Workable, Eatable):
    def work(self):
        return "Human is working"

    def eat(self):
        return "Human is eating"

# A robot only implements what it needs
class Robot(Workable):
    def work(self):
        return "Robot is working"
Why is this better?
✔ Human and Robot only implement what they actually need.
✔ The interfaces are now **small & specific