# Clean Code

Clean code is code whose intent can be understood with little effort. It is not code with the fewest characters, the most comments, or the largest number of tiny functions.

## 1. Name things for their meaning

Names should reveal domain intent and distinguish concepts that are not interchangeable.

```python
# Unclear
x = price * q

# Clear
line_total = unit_price * quantity
```

Avoid encoding implementation details in names when the detail may change. `orders_by_customer` is often more useful than `orders_dict`.

## 2. Keep functions focused

A function is easier to reason about when it performs one coherent task at one level of abstraction.

```python
def calculate_line_total(unit_price: Decimal, quantity: int) -> Decimal:
    if quantity <= 0:
        raise ValueError("quantity must be positive")
    return unit_price * quantity
```

A function can contain several steps when those steps all contribute to one clear operation. Do not split code mechanically just to make every function three lines long.

## 3. Make invalid states difficult to represent

Validate important invariants at the boundary where data enters the domain. A valid `OrderItem` should not exist with a zero quantity. This moves checks closer to the source of invalid data and reduces repeated defensive code.

## 4. Reduce hidden side effects

A function that looks like a calculation should not also send an email or write to a database. Separate computation from orchestration so the computation can be tested directly.

Prefer explicit dependencies:

```python
class ReportService:
    def __init__(self, repository: ReportRepository) -> None:
        self._repository = repository
```

This makes the service's collaborators visible and replaceable.

## 5. Comments should add information

Useful comments explain *why* a surprising decision exists, a constraint that is not obvious from code, or a non-obvious algorithm. Comments that merely translate each line into English become stale quickly.

```python
# Keep the original amount for audit history; discounting changes only the payable total.
```

## 6. Avoid boolean arguments that hide meaning

A call such as `send_report(report, True)` makes the caller's intent unclear. Consider a named option, two explicit methods, or a small configuration object. Do not over-engineer a one-off helper when the meaning is already obvious.

## 7. Keep related data and behavior together

If a rule always needs the same data, consider whether that rule belongs with the data. `Order.subtotal` belongs naturally on `Order`, while coordinating payment, persistence, and notification belongs in an application service.

## 8. Prefer simple control flow

Use guard clauses to handle invalid or exceptional cases early. Avoid deeply nested conditionals and clever expressions that require a reader to mentally simulate several branches.

## Practical review questions

- Can a reader infer the purpose from the name and signature?
- Are inputs validated once, at a meaningful boundary?
- Are side effects obvious?
- Does each function operate at a consistent level of abstraction?
- Is a comment explaining a reason, or just repeating the code?
- Would a small change require editing unrelated responsibilities?

Clean code is a continuous maintenance practice. Optimize for the next person who must safely change the code, including your future self.
