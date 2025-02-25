# Liskov Substitution Principle (LSP)

## Explanation  
The **Liskov Substitution Principle (LSP)** states that **subtypes must be replaceable** for their base types **without affecting functionality**.

---

## Bad Example – Violating LSP:
```python
class Bird:
    def fly(self):
        return "Flying"

class Penguin(Bird):
    def fly(self):
        raise Exception("Penguins cannot fly")
Problem:
The Penguin class breaks the behavior of Bird because it cannot fly.

Good Example – Applying LSP:
class Bird:
    pass

class FlyingBird(Bird):
    def fly(self):
        return "Flying"

class Penguin(Bird):
    def swim(self):
        return "Swimming"
Why is this better?
✔ Now, Penguin does not inherit behavior it cannot fulfill.
✔ Each subclass respects the contract of the base class.