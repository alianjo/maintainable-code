from decimal import Decimal

import pytest

from maintainable_shop.application.checkout import CheckoutService
from maintainable_shop.application.discounts import PercentageDiscount
from maintainable_shop.domain.exceptions import DomainError, PaymentDeclinedError
from maintainable_shop.domain.money import Money
from maintainable_shop.infrastructure.fakes import (
    FakePaymentGateway,
    RecordingNotifier,
)
from maintainable_shop.infrastructure.in_memory import InMemoryOrderRepository


def build_service(*, should_decline: bool = False) -> tuple:
    repository = InMemoryOrderRepository()
    payment = FakePaymentGateway(should_decline=should_decline)
    notifier = RecordingNotifier()
    service = CheckoutService(
        repository,
        payment,
        notifier,
        PercentageDiscount(Decimal("0.10")),
    )
    return service, repository, payment, notifier


def test_checkout_returns_expected_totals_and_reference(make_order) -> None:
    service, repository, payment, notifier = build_service()

    result = service.place_order(make_order())

    assert result.subtotal == Money(Decimal("60.00"))
    assert result.discount == Money(Decimal("6.00"))
    assert result.payable_total == Money(Decimal("54.00"))
    assert result.payment_reference == "fake-payment-0001"
    assert repository.get("order-1") is not None
    assert len(payment.charges) == 1
    assert len(notifier.confirmations) == 1


def test_declined_payment_does_not_save_or_notify(make_order) -> None:
    service, repository, payment, notifier = build_service(should_decline=True)

    with pytest.raises(PaymentDeclinedError):
        service.place_order(make_order())

    assert len(repository) == 0
    assert payment.charges == []
    assert notifier.confirmations == []


def test_checkout_allows_a_full_discount(make_order) -> None:
    repository = InMemoryOrderRepository()
    payment = FakePaymentGateway()
    notifier = RecordingNotifier()
    service = CheckoutService(
        repository,
        payment,
        notifier,
        PercentageDiscount(Decimal("1.00")),
    )

    result = service.place_order(make_order())

    assert result.payable_total == Money.zero("USD")
    assert payment.charges[0][1] == Money.zero("USD")


def test_checkout_rejects_discount_larger_than_subtotal(make_order) -> None:
    class ExcessiveDiscountPolicy:
        def discount_for(self, order):
            return Money(Decimal("61.00"), "USD")

    repository = InMemoryOrderRepository()
    payment = FakePaymentGateway()
    notifier = RecordingNotifier()
    service = CheckoutService(repository, payment, notifier, ExcessiveDiscountPolicy())

    with pytest.raises(DomainError, match="cannot exceed"):
        service.place_order(make_order())

    assert payment.charges == []
    assert len(repository) == 0


def test_checkout_does_not_charge_when_discount_currency_is_invalid(make_order) -> None:
    class WrongCurrencyPolicy:
        def discount_for(self, order):
            return Money(Decimal("1.00"), "EUR")

    repository = InMemoryOrderRepository()
    payment = FakePaymentGateway()
    notifier = RecordingNotifier()
    service = CheckoutService(repository, payment, notifier, WrongCurrencyPolicy())

    with pytest.raises(DomainError, match="discount currency"):
        service.place_order(make_order())

    assert payment.charges == []
    assert len(repository) == 0
