# Exercises

Try these after understanding the existing example. Make one change at a time and add tests before changing implementation.

## Beginner

1. Add a `FixedAmountDiscount` policy. Validate that its amount cannot be negative and cannot exceed the order subtotal.
2. Add tests for an order containing multiple items with different prices.
3. Improve the demo so the discount policy can be selected through a small, explicit configuration value.

## Intermediate

4. Add a `CurrencyMismatchError` test for applying a discount in a different currency.
5. Define a repository contract test that can be reused by multiple repository adapters.
6. Add an order status value object or enum. Decide which layer owns allowed state transitions and test them.
7. Add structured application logging at the orchestration boundary. Do not log payment credentials or unnecessary personal data.

## Advanced design discussion

8. The sample charges a payment before persisting the order. Explain what happens if persistence fails after the charge succeeds. Propose an idempotency and reconciliation strategy.
9. Design an outbox-based notification flow. Identify the transaction boundary and how retries avoid duplicate messages.
10. Replace the in-memory repository with a database adapter. Keep database models and migrations outside the domain layer.
11. Add a real payment-provider adapter behind `PaymentGateway`. Define timeout, retry, idempotency, and secret-management requirements before implementing it.

## Reflection

For each exercise, answer:

- Which behavior changed?
- Which module owns that behavior?
- What test gives confidence in the change?
- Did the new abstraction reduce coupling, or merely add indirection?
