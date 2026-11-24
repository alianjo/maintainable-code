from decimal import Decimal

import pytest

from maintainable_shop.domain.exceptions import InvalidOrderError
from maintainable_shop.domain.money import Money
from maintainable_shop.domain.order import Order, OrderItem


def test_order_item_calculates_line_total() -> None:
    item = OrderItem("pen-1", "Pen", Money(Decimal("2.50")), 4)
    assert item.line_total == Money(Decimal("10.00"))


def test_order_calculates_subtotal_for_multiple_items() -> None:
    order = Order(
        order_id="order-2",
        customer_id="customer-2",
        customer_email="person@example.com",
        items=(
            OrderItem("pen", "Pen", Money(Decimal("2.50")), 2),
            OrderItem("book", "Book", Money(Decimal("10.00")), 1),
        ),
    )
    assert order.subtotal == Money(Decimal("15.00"))


def test_order_rejects_empty_items() -> None:
    with pytest.raises(InvalidOrderError, match="at least one item"):
        Order("order-3", "customer-3", "person@example.com", ())


def test_order_item_rejects_zero_quantity() -> None:
    with pytest.raises(InvalidOrderError, match="greater than zero"):
        OrderItem("pen", "Pen", Money(Decimal("2.50")), 0)


def test_order_rejects_items_with_different_currencies() -> None:
    items = (
        OrderItem("book", "Book", Money(Decimal("10.00"), "USD"), 1),
        OrderItem("map", "Map", Money(Decimal("8.00"), "EUR"), 1),
    )
    with pytest.raises(InvalidOrderError, match="same currency"):
        Order("order-4", "customer-4", "person@example.com", items)


def test_order_rejects_blank_customer_identifier() -> None:
    item = OrderItem("pen", "Pen", Money(Decimal("2.50")), 1)
    with pytest.raises(InvalidOrderError, match="customer_id"):
        Order("order-5", " ", "person@example.com", (item,))


def test_order_item_rejects_boolean_quantity() -> None:
    with pytest.raises(TypeError, match="integer"):
        OrderItem("pen", "Pen", Money(Decimal("2.50")), True)
