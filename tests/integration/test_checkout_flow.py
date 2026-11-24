from decimal import Decimal

from maintainable_shop.application.checkout import CheckoutService
from maintainable_shop.application.discounts import NoDiscount
from maintainable_shop.domain.money import Money
from maintainable_shop.domain.order import Order, OrderItem
from maintainable_shop.infrastructure.fakes import (
    FakePaymentGateway,
    RecordingNotifier,
)
from maintainable_shop.infrastructure.in_memory import InMemoryOrderRepository


def test_checkout_flow_persists_order_and_records_confirmation() -> None:
    order = Order(
        order_id="integration-order-1",
        customer_id="integration-customer",
        customer_email="integration@example.com",
        items=(OrderItem("sku-1", "Notebook", Money(Decimal("7.50")), 2),),
    )
    repository = InMemoryOrderRepository()
    gateway = FakePaymentGateway()
    notifier = RecordingNotifier()
    checkout = CheckoutService(repository, gateway, notifier, NoDiscount())

    result = checkout.place_order(order)

    stored = repository.get("integration-order-1")
    assert stored is not None
    assert stored.order == order
    assert stored.payable_total == Money(Decimal("15.00"))
    assert stored.payment_reference == result.payment_reference
    assert notifier.confirmations[0].order_id == order.order_id
    assert notifier.confirmations[0].payable_total == result.payable_total
