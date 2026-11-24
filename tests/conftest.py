"""Shared test factories."""

from decimal import Decimal

import pytest

from maintainable_shop.domain.money import Money
from maintainable_shop.domain.order import Order, OrderItem


@pytest.fixture
def make_order():
    """Create an order with a predictable subtotal for a test."""

    def factory(
        *,
        order_id: str = "order-1",
        items: tuple[OrderItem, ...] | None = None,
    ) -> Order:
        selected_items = items or (
            OrderItem(
                product_id="book-1",
                name="Clean Architecture",
                unit_price=Money(Decimal("30.00"), "USD"),
                quantity=2,
            ),
        )
        return Order(
            order_id=order_id,
            customer_id="customer-1",
            customer_email="reader@example.com",
            items=selected_items,
        )

    return factory
