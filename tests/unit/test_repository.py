from decimal import Decimal

import pytest

from maintainable_shop.domain.exceptions import DuplicateOrderError
from maintainable_shop.domain.money import Money
from maintainable_shop.infrastructure.in_memory import InMemoryOrderRepository


def test_repository_stores_and_retrieves_order(make_order) -> None:
    repository = InMemoryOrderRepository()
    order = make_order()
    payable_total = Money(Decimal("54.00"), "USD")

    repository.save(order, payable_total, "payment-1")

    stored = repository.get(order.order_id)
    assert stored is not None
    assert stored.order == order
    assert stored.payable_total == payable_total
    assert stored.payment_reference == "payment-1"


def test_repository_rejects_duplicate_order_identifier(make_order) -> None:
    repository = InMemoryOrderRepository()
    order = make_order()
    total = Money(Decimal("60.00"), "USD")
    repository.save(order, total, "payment-1")

    with pytest.raises(DuplicateOrderError, match="already exists"):
        repository.save(order, total, "payment-2")


def test_repository_returns_none_for_unknown_order() -> None:
    assert InMemoryOrderRepository().get("missing") is None
