# SOLID principles

SOLID is a set of design heuristics for managing change in object-oriented systems. The principles are not commands to create an interface and class for every operation. Apply them when they reduce real coupling or make likely changes safer.

## S — Single Responsibility Principle

A module should have one cohesive responsibility and one primary reason to change.

A class that calculates an invoice, writes a PDF, emails a customer, and stores a database row has several unrelated reasons to change. Separate the calculation from output and persistence. The application layer can coordinate those pieces.

**Ask:** Which kind of requirement would cause this module to change? Are those requirements related?

## O — Open/Closed Principle

A component should allow useful extension without requiring edits to stable logic every time a new variation is introduced.

A discount policy can be represented by a small contract:

```python
from typing import Protocol


class DiscountPolicy(Protocol):
    def discount_for(self, subtotal: Money) -> Money: ...
```

A percentage discount can be added as another implementation. The checkout use case can depend on the contract instead of knowing every discount type.

**Trade-off:** Do not build an extension framework for variations that are unlikely to exist. A simple conditional may be clearer for two stable cases.

## L — Liskov Substitution Principle

An implementation used in place of an abstraction must honor the abstraction's behavioral expectations. Matching method names is not enough.

If a repository promises that `save` stores an order and makes it retrievable, an implementation that silently drops some valid orders violates the contract. Tests should verify observable behavior, not implementation details.

**Ask:** Can every implementation be substituted without surprising callers or weakening guarantees?

## I — Interface Segregation Principle

Callers should not depend on methods they do not need. Prefer small, role-based contracts over one large interface containing unrelated operations.

A checkout operation may need `charge`, but it does not need a payment gateway's refund reporting, settlement exports, or administrative methods. Keep the checkout-facing contract narrow.

## D — Dependency Inversion Principle

High-level policy should not depend directly on low-level details. Both should depend on abstractions that describe the required behavior.

In the sample application, `CheckoutService` depends on `OrderRepository`, `PaymentGateway`, and `OrderNotifier` protocols. In-memory implementations live in the infrastructure package and can be replaced without rewriting the use case.

Dependency inversion is about the direction of source-code dependencies—not simply passing a concrete object into a constructor.

## Putting the principles together

1. Identify a responsibility that changes for a different reason.
2. Extract a small boundary only when callers need a stable contract.
3. Make the high-level policy depend on that contract.
4. Add a second implementation or test double to prove the boundary is useful.
5. Keep the abstraction as small as the use case requires.

The best design is the simplest design that keeps expected changes localized.
