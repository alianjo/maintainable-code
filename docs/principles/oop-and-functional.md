# Object-Oriented and Functional Programming

Object-oriented programming (OOP) and functional programming (FP) are ways to organize behavior and manage state. They are not mutually exclusive, and a maintainable Python application often uses ideas from both.

## Object-oriented programming

OOP groups data and behavior into objects. It is useful when the domain contains entities with identity, invariants, and behavior that belongs with their state.

```python
from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class OrderLine:
    unit_price: Decimal
    quantity: int

    def total(self) -> Decimal:
        if self.quantity <= 0:
            raise ValueError("quantity must be positive")
        return self.unit_price * self.quantity
```

The `OrderLine` object owns the rule for calculating its line total and validates its quantity. Encapsulation protects the invariant from being reimplemented inconsistently by callers.

## Functional programming

Functional programming emphasizes transformations, explicit inputs and outputs, and minimizing hidden state changes. Pure functions return the same result for the same inputs and do not modify external state.

```python
from decimal import Decimal


def calculate_subtotal(line_totals: tuple[Decimal, ...]) -> Decimal:
    return sum(line_totals, start=Decimal("0.00"))
```

This calculation is easy to test because it has no network, database, or global-state dependency.

## Immutability

Immutable values are easier to share because callers cannot unexpectedly change them. The sample uses frozen dataclasses for `Money`, `OrderItem`, and `Order`. Immutability is especially useful for value objects and messages, but it is not always practical for every part of an application.

## Where side effects belong

A useful design is to keep core calculations deterministic and isolate side effects at the edges:

- Domain objects enforce business rules.
- Pure functions calculate values and transform data.
- Application services coordinate a use case.
- Infrastructure adapters perform database, network, file, and messaging operations.

The checkout example combines both styles: immutable domain objects and calculation-oriented discount policies are coordinated by an object-oriented application service.

## Choosing an approach

Use OOP when identity, lifecycle, and invariants make a cohesive object helpful. Use pure functions when a transformation is naturally described by inputs and outputs. Use both when that makes the responsibilities clearer.

Avoid turning every function into a class, and avoid building a large chain of anonymous transformations when a named domain operation would be easier to understand.
