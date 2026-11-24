"""Run a complete checkout with in-memory adapters."""

from decimal import Decimal

from maintainable_shop.application.checkout import CheckoutService
from maintainable_shop.application.discounts import PercentageDiscount
from maintainable_shop.domain.money import Money
from maintainable_shop.domain.order import Order, OrderItem
from maintainable_shop.infrastructure.fakes import (
    FakePaymentGateway,
    RecordingNotifier,
)
from maintainable_shop.infrastructure.in_memory import InMemoryOrderRepository


def main() -> None:
    order = Order(
        order_id="order-1001",
        customer_id="customer-42",
        customer_email="customer@example.com",
        items=(
            OrderItem(
                product_id="keyboard-01",
                name="Mechanical keyboard",
                unit_price=Money(Decimal("80.00"), "USD"),
                quantity=1,
            ),
            OrderItem(
                product_id="mouse-02",
                name="Wireless mouse",
                unit_price=Money(Decimal("25.00"), "USD"),
                quantity=2,
            ),
        ),
    )

    repository = InMemoryOrderRepository()
    payment_gateway = FakePaymentGateway()
    notifier = RecordingNotifier()
    checkout = CheckoutService(
        repository=repository,
        payment_gateway=payment_gateway,
        notifier=notifier,
        discount_policy=PercentageDiscount(Decimal("0.10")),
    )

    result = checkout.place_order(order)
    print(f"Order: {result.order_id}")
    print(f"Subtotal: {result.subtotal}")
    print(f"Discount: {result.discount}")
    print(f"Paid: {result.payable_total}")
    print(f"Payment reference: {result.payment_reference}")
    print(f"Saved orders: {len(repository)}")
    print(f"Notifications sent: {len(notifier.confirmations)}")


if __name__ == "__main__":
    main()
