# Design patterns: use them with intent

A design pattern is a named, reusable approach to a recurring design problem. A pattern is useful when it makes a real variation or relationship easier to understand. It is not a badge of sophistication.

## Strategy

Encapsulates interchangeable algorithms behind a common interface. `NoDiscount` and `PercentageDiscount` are strategies: the checkout flow uses either without embedding the discount formula in the use case.

Use it when behavior varies independently and the caller should not know each implementation's details.

## Repository

Provides a collection-like boundary for retrieving or storing domain objects. `OrderRepository` is a port; `InMemoryOrderRepository` is one adapter.

Use it when persistence should be replaceable or when the boundary protects the domain from storage details. Do not create repository classes for every table automatically.

## Dependency Injection

Supplies an object's collaborators from the outside rather than constructing them internally. `CheckoutService` receives its dependencies in `__init__`.

Constructor injection is explicit and easy to test. A global service locator usually hides dependencies and makes tests harder to reason about.

## Adapter

Converts one interface into another. A real payment adapter could translate the application's `PaymentGateway` contract into an external provider's SDK calls. The sample fake adapters are deliberately simple.

## Factory

Centralizes object creation when construction is complex or depends on configuration. A factory is unnecessary when `ClassName(...)` is already clear.

## How to choose

Ask what is changing, who needs to know about the change, and whether a stable contract reduces coupling. If a pattern adds more indirection than it removes, keep the simpler design.
