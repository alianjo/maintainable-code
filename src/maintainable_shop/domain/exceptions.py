"""Domain-specific exceptions."""


class DomainError(ValueError):
    """Base class for invalid domain operations."""


class CurrencyMismatchError(DomainError):
    """Raised when money values with different currencies are combined."""


class InvalidOrderError(DomainError):
    """Raised when an order violates a business invariant."""


class DuplicateOrderError(DomainError):
    """Raised when an order with the same identifier is stored twice."""


class PaymentDeclinedError(Exception):
    """Raised when a payment provider declines a charge."""
