# Error handling and logging

Good error handling makes failure behavior explicit. Logging helps operators understand what happened in a running system. Neither should be used to hide unclear control flow.

## Raise meaningful exceptions

Use exceptions to report invalid states or failures that a caller can handle. Prefer a specific exception when it changes how the caller should respond.

```python
class PaymentDeclinedError(Exception):
    """The payment provider declined the attempted charge."""
```

Do not catch every exception and return `None`. That often turns a clear failure into a later, confusing error.

## Catch exceptions at the boundary that can respond

A lower-level function should generally raise an error with useful context or let it propagate. The layer that can retry, show a safe message, choose a fallback, or stop a workflow should decide how to handle it.

Avoid broad handlers such as `except Exception: pass`. When catching a broad exception at a process boundary, log it with context and preserve the failure signal or return a deliberate error response.

## Keep error messages safe

Error messages shown to users should not reveal credentials, payment tokens, personal records, SQL details, or internal infrastructure information. Keep detailed diagnostic data in access-controlled logs and redact secrets.

## Use structured, contextual logs

Prefer stable event names and useful identifiers over long interpolated prose. Include request or correlation identifiers where available. Do not log full payment data, authentication tokens, or sensitive customer content.

Example:

```python
import logging

logger = logging.getLogger(__name__)


def log_checkout_failure(order_id: str, reason: str) -> None:
    logger.warning(
        "checkout_failed",
        extra={"order_id": order_id, "failure_reason": reason},
    )
```

Configure handlers, levels, and output formats at the application entry point. Libraries should normally use `logging.getLogger(__name__)` and leave global logging configuration to the application.

## Retry with care

Retries are appropriate only when the operation is safe to retry or protected by an idempotency mechanism. Retrying a payment charge without an idempotency key can charge a customer twice. Use bounded retries, timeouts, and observability; do not retry every exception indiscriminately.

## Practical questions

- Can the caller distinguish validation errors from infrastructure failures?
- Is the exception caught by a layer that can take meaningful action?
- Does the log contain enough context to investigate the event?
- Could the log expose credentials or personal information?
- Is a retry safe, bounded, and observable?
