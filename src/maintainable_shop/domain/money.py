"""Immutable money value object with explicit currency handling."""

from dataclasses import dataclass
from decimal import Decimal

from maintainable_shop.domain.exceptions import CurrencyMismatchError, DomainError


@dataclass(frozen=True, slots=True)
class Money:
    """An amount and its ISO-style three-letter currency code.

    This teaching example assumes two fractional digits for percentage
    calculations. A production financial system must account for currency-
    specific minor units and provider rounding rules.
    """

    amount: Decimal
    currency: str = "USD"

    def __post_init__(self) -> None:
        if not isinstance(self.amount, Decimal):
            raise TypeError("amount must be a Decimal; do not use float for money")
        if not self.amount.is_finite():
            raise DomainError("amount must be finite")
        normalized_currency = self.currency.strip().upper()
        if len(normalized_currency) != 3 or not normalized_currency.isalpha():
            raise DomainError("currency must be a three-letter code")
        if self.amount < 0:
            raise DomainError("money amount cannot be negative")
        object.__setattr__(self, "currency", normalized_currency)

    @classmethod
    def zero(cls, currency: str = "USD") -> "Money":
        """Create a zero amount in the requested currency."""
        return cls(Decimal("0.00"), currency)

    def _ensure_same_currency(self, other: "Money") -> None:
        if self.currency != other.currency:
            raise CurrencyMismatchError(
                f"cannot combine {self.currency} with {other.currency}"
            )

    def __add__(self, other: "Money") -> "Money":
        self._ensure_same_currency(other)
        return Money(self.amount + other.amount, self.currency)

    def __sub__(self, other: "Money") -> "Money":
        self._ensure_same_currency(other)
        result = self.amount - other.amount
        if result < 0:
            raise DomainError("money result cannot be negative")
        return Money(result, self.currency)

    def multiply(self, quantity: int) -> "Money":
        """Multiply by a non-negative integer quantity."""
        if isinstance(quantity, bool) or not isinstance(quantity, int):
            raise TypeError("quantity must be an integer")
        if quantity < 0:
            raise DomainError("quantity cannot be negative")
        return Money(self.amount * quantity, self.currency)

    def __str__(self) -> str:
        return f"{self.amount:.2f} {self.currency}"
