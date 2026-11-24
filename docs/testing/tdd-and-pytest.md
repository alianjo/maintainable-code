# Testing and Test-Driven Development

Tests provide feedback about observable behavior. A useful test gives a developer confidence to change code while preserving the behavior that matters.

## Test levels

### Unit tests

Exercise a small unit in isolation. They are useful for domain rules, calculations, and validation. Examples live in `tests/unit`.

### Integration tests

Exercise multiple components together across a meaningful boundary. The checkout integration test wires the real use case with in-memory adapters. It does not contact external services.

### End-to-end tests

Exercise a deployed application through its public interface, often including a browser or HTTP client. This repository does not need an end-to-end environment because its example has no web interface.

Choose the smallest test level that proves the behavior. Do not build a large integration test to verify a pure calculation.

## Arrange, Act, Assert

A readable test generally has three stages:

```python
def test_percentage_discount_reduces_subtotal() -> None:
    # Arrange
    order = make_order(subtotal="100.00")
    policy = PercentageDiscount(Decimal("0.10"))

    # Act
    discount = policy.discount_for(order)

    # Assert
    assert discount == Money(Decimal("10.00"), "USD")
```

Use fixtures and helpers to remove repetitive setup, but do not hide the behavior under test behind a complicated fixture hierarchy.

## TDD: Red, Green, Refactor

1. **Red:** write one test describing the next behavior and confirm it fails for the expected reason.
2. **Green:** write the smallest implementation that makes the test pass.
3. **Refactor:** improve names or structure while keeping the tests green.

TDD is a feedback loop, not a requirement to predict every implementation detail before coding. Tests should describe behavior, not mirror private methods.

## Test doubles

- **Stub:** returns canned data needed by a test.
- **Fake:** has a lightweight working implementation, such as an in-memory repository.
- **Mock:** verifies an expected interaction. Use it when the interaction itself is part of the behavior.
- **Spy:** records calls so a test can inspect them later.

Prefer simple fakes and recording objects for most application tests. Excessive mocking couples tests to internal call sequences and makes refactoring harder.

## What should be tested?

- Valid and invalid inputs at boundaries.
- Domain invariants and calculation edge cases.
- Observable outcomes of use cases.
- Failure paths that affect business behavior.
- Contract behavior shared by multiple implementations.

Do not test every getter, private method, or line simply to raise coverage. Coverage is a signal about what ran, not proof that assertions are meaningful.
