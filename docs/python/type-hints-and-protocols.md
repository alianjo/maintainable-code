# Python type hints, dataclasses, and Protocols

Type hints document expected values and help static tools detect inconsistent usage. Python does not enforce most annotations at runtime, so validate external input where it enters the application.

## Use types to communicate intent

Prefer a domain type over a vague primitive when the value has rules of its own. `Money` communicates amount and currency together and can enforce arithmetic rules centrally.

## Dataclasses for data with behavior

`@dataclass(frozen=True, slots=True)` is useful for small immutable domain values. It generates common methods while keeping invariants in `__post_init__`. Do not use a dataclass automatically for every class; services with behavior and dependencies may be ordinary classes.

## Protocols for structural contracts

```python
from typing import Protocol


class PaymentGateway(Protocol):
    def charge(self, customer_id: str, amount: Money) -> str: ...
```

A class satisfies this protocol by providing a compatible method. It does not need to inherit from `PaymentGateway`. This keeps application code independent of implementation inheritance.

## Avoid `Any` as a shortcut

`Any` disables much of the value of static checking. Prefer precise types, generics, `object` for genuinely unknown values, or a validation step that converts external data into a domain type.

## Keep runtime validation

A type annotation such as `quantity: int` does not prevent a caller from passing `0`, `-1`, or `True`. Validate business invariants explicitly. The sample's `OrderItem` does this at construction time.

## Practical guidance

- Add annotations to public functions and important boundaries.
- Use `Decimal` for money-like decimal calculations, not binary floating-point values.
- Use `Enum` for a closed set of meaningful states.
- Use `Protocol` when a caller needs behavior but should not depend on a concrete class.
- Avoid type gymnastics that make straightforward code difficult to read.
