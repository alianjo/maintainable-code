from decimal import Decimal

import pytest

from maintainable_shop.application.discounts import NoDiscount, PercentageDiscount
from maintainable_shop.domain.exceptions import DomainError
from maintainable_shop.domain.money import Money
from maintainable_shop.domain.order import OrderItem


def test_no_discount_returns_zero_in_order_currency(make_order) -> None:
    order = make_order(
        items=(OrderItem("sku", "Item", Money(Decimal("12.00"), "EUR"), 1),)
    )
    assert NoDiscount().discount_for(order) == Money.zero("EUR")


def test_percentage_discount_calculates_expected_amount(make_order) -> None:
    discount = PercentageDiscount(Decimal("0.10"))
    assert discount.discount_for(make_order()) == Money(Decimal("6.00"), "USD")


def test_percentage_discount_rounds_half_up(make_order) -> None:
    order = make_order(items=(OrderItem("sku", "Item", Money(Decimal("1.05")), 1),))
    assert PercentageDiscount(Decimal("0.10")).discount_for(order) == Money(
        Decimal("0.11"), "USD"
    )


@pytest.mark.parametrize("rate", [Decimal("-0.01"), Decimal("1.01")])
def test_percentage_discount_rejects_out_of_range_rate(rate: Decimal) -> None:
    with pytest.raises(DomainError, match="between 0 and 1"):
        PercentageDiscount(rate)
