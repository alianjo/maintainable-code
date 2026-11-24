"""Simple fake adapters for local demos and automated tests."""

from dataclasses import dataclass

from maintainable_shop.domain.exceptions import PaymentDeclinedError
from maintainable_shop.domain.money import Money
from maintainable_shop.domain.order import Order


class FakePaymentGateway:
    """A deterministic payment fake that can simulate a decline."""

    def __init__(self, *, should_decline: bool = False) -> None:
        self.should_decline = should_decline
        self.charges: list[tuple[str, Money]] = []

    def charge(self, customer_id: str, amount: Money) -> str:
        if self.should_decline:
            raise PaymentDeclinedError("payment was declined")
        self.charges.append((customer_id, amount))
        return f"fake-payment-{len(self.charges):04d}"


@dataclass(frozen=True, slots=True)
class Confirmation:
    """A recorded confirmation for test and demo inspection."""

    order_id: str
    payable_total: Money
    payment_reference: str


class RecordingNotifier:
    """Records notifications instead of sending real messages."""

    def __init__(self) -> None:
        self.confirmations: list[Confirmation] = []

    def send_order_confirmation(
        self, order: Order, payable_total: Money, payment_reference: str
    ) -> None:
        self.confirmations.append(
            Confirmation(
                order_id=order.order_id,
                payable_total=payable_total,
                payment_reference=payment_reference,
            )
        )
