# Layered architecture and dependency direction

The example uses three conceptual layers. The names are not important; the dependency direction is.

```text
Presentation / entry point (demo.py)
             |
             v
Application (checkout use case, ports)
             |
             v
Domain (orders, money, business invariants)

Infrastructure adapters implement application ports:
- in-memory order repository
- fake payment gateway
- recording notifier
```

## Domain layer

The domain contains business language and invariants. It should not import web frameworks, ORM models, environment variables, or network clients. In this project, `Money`, `Order`, and `OrderItem` are plain Python objects.

## Application layer

The application layer expresses a use case: coordinate the domain and the outside capabilities required to complete a task. It defines ports (`Protocol` types) for those capabilities. The use case should not know whether an order is saved to PostgreSQL or an in-memory dictionary.

## Infrastructure layer

Infrastructure contains implementation details: database repositories, HTTP clients, message brokers, file systems, and external SDKs. The sample uses in-memory adapters so it runs with no infrastructure setup.

## Composition root

At the edge of the application, concrete dependencies are assembled. `demo.py` is the composition root for the example. The service itself does not instantiate its repository, payment gateway, or notifier.

## What should depend on what?

- Domain should not depend on application or infrastructure.
- Application may depend on domain and its own contracts.
- Infrastructure may depend on application contracts and domain types to implement those contracts.
- The entry point may import all layers to wire them together.

This is a small ports-and-adapters / hexagonal architecture example. It is not necessary to use this architecture for every script or CRUD endpoint. Add boundaries when they protect meaningful business rules or isolate volatile details.

## A production concern: distributed consistency

The checkout sample charges a payment and then saves the order. A real payment provider and a real database do not share one atomic transaction. A database failure after a successful charge can leave the system inconsistent. Production systems need explicit strategies such as idempotency keys, durable payment states, retries, reconciliation, and often an outbox or saga. The in-memory sample intentionally does not claim to solve this problem.
