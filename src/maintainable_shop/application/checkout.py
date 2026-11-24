"""Checkout use case: coordinate policies and external capabilities."""

from dataclasses import dataclass

from maintainable_shop.application.ports import (
    DiscountPolicy,
    OrderNotifier,
    OrderRepository,
    PaymentGateway,
)
from maintainable_shop.domain.exceptions import DomainError
from maintainable_shop.domain.money import Money
from maintainable_shop.domain.order import Order


@dataclass(frozen=True, slots=True)
class CheckoutResult:
    """The public result of a successful checkout."""

    order_id: str
    subtotal: Money
    discount: Money
    payable_total: Money
    payment_reference: str


class CheckoutService:
    """Place an order without depending on concrete infrastructure classes."""

    def __init__(
        self,
        repository: OrderRepository,
        payment_gateway: PaymentGateway,
        notifier: OrderNotifier,
        discount_policy: DiscountPolicy,
    ) -> None:
        self._repository = repository
        self._payment_gateway = payment_gateway
        self._notifier = notifier
        self._discount_policy = discount_policy

    def place_order(self, order: Order) -> CheckoutResult:
        """Charge, persist, and notify for an order.

        A declined payment stops the workflow before persistence or notification.
        Real systems need a durable state machine and idempotency strategy to
        handle failures between external side effects; see the architecture guide.
        """
        subtotal = order.subtotal
        discount = self._discount_policy.discount_for(order)
        if discount.currency != subtotal.currency:
            raise DomainError("discount currency must match the order currency")
        if discount.amount > subtotal.amount:
            raise DomainError("discount cannot exceed the order subtotal")

        payable_total = subtotal - discount
        payment_reference = self._payment_gateway.charge(
            order.customer_id, payable_total
        )
        self._repository.save(order, payable_total, payment_reference)
        self._notifier.send_order_confirmation(order, payable_total, payment_reference)

        return CheckoutResult(
            order_id=order.order_id,
            subtotal=subtotal,
            discount=discount,
            payable_total=payable_total,
            payment_reference=payment_reference,
        )
