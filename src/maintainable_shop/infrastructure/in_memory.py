"""In-memory adapters; useful for learning and tests, not durable storage."""

from dataclasses import dataclass

from maintainable_shop.domain.exceptions import DuplicateOrderError
from maintainable_shop.domain.money import Money
from maintainable_shop.domain.order import Order


@dataclass(frozen=True, slots=True)
class SavedOrder:
    """An order and the outcome recorded by the checkout use case."""

    order: Order
    payable_total: Money
    payment_reference: str


class InMemoryOrderRepository:
    """A simple repository implementation backed by a dictionary."""

    def __init__(self) -> None:
        self._orders: dict[str, SavedOrder] = {}

    def save(self, order: Order, payable_total: Money, payment_reference: str) -> None:
        if order.order_id in self._orders:
            raise DuplicateOrderError(f"order {order.order_id!r} already exists")
        self._orders[order.order_id] = SavedOrder(
            order=order,
            payable_total=payable_total,
            payment_reference=payment_reference,
        )

    def get(self, order_id: str) -> SavedOrder | None:
        """Return a saved order, or ``None`` when it does not exist."""
        return self._orders.get(order_id)

    def __len__(self) -> int:
        return len(self._orders)
