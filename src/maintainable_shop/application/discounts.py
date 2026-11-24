"""Discount strategies used by the checkout use case."""

from dataclasses import dataclass
from decimal import ROUND_HALF_UP, Decimal

from maintainable_shop.domain.exceptions import DomainError
from maintainable_shop.domain.money import Money
from maintainable_shop.domain.order import Order

_CENT = Decimal("0.01")


@dataclass(frozen=True, slots=True)
class NoDiscount:
    """A policy that does not reduce the subtotal."""

    def discount_for(self, order: Order) -> Money:
        return Money.zero(order.subtotal.currency)


@dataclass(frozen=True, slots=True)
class PercentageDiscount:
    """A discount rate expressed as a fraction from zero to one."""

    rate: Decimal

    def __post_init__(self) -> None:
        if not isinstance(self.rate, Decimal):
            raise TypeError("rate must be a Decimal")
        if not self.rate.is_finite() or not Decimal("0") <= self.rate <= Decimal("1"):
            raise DomainError("rate must be between 0 and 1")

    def discount_for(self, order: Order) -> Money:
        subtotal = order.subtotal
        amount = (subtotal.amount * self.rate).quantize(_CENT, rounding=ROUND_HALF_UP)
        return Money(amount, subtotal.currency)
