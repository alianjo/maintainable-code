"""Small contracts required by application use cases."""

from typing import Protocol

from maintainable_shop.domain.money import Money
from maintainable_shop.domain.order import Order


class DiscountPolicy(Protocol):
    """Calculates a discount for an order."""

    def discount_for(self, order: Order) -> Money:
        """Return the discount in the order's currency."""


class OrderRepository(Protocol):
    """Stores completed orders."""

    def save(self, order: Order, payable_total: Money, payment_reference: str) -> None:
        """Persist the order and its payment reference."""


class PaymentGateway(Protocol):
    """Charges a customer through a payment provider."""

    def charge(self, customer_id: str, amount: Money) -> str:
        """Charge the customer and return a provider reference."""


class OrderNotifier(Protocol):
    """Sends a confirmation after an order has been placed."""

    def send_order_confirmation(
        self, order: Order, payable_total: Money, payment_reference: str
    ) -> None:
        """Notify the customer about a completed checkout."""
