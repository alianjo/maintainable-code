"""Order entities and their invariants."""

from dataclasses import dataclass

from maintainable_shop.domain.exceptions import InvalidOrderError
from maintainable_shop.domain.money import Money


@dataclass(frozen=True, slots=True)
class OrderItem:
    """A purchasable line in an order."""

    product_id: str
    name: str
    unit_price: Money
    quantity: int

    def __post_init__(self) -> None:
        if not self.product_id.strip():
            raise InvalidOrderError("product_id cannot be empty")
        if not self.name.strip():
            raise InvalidOrderError("name cannot be empty")
        if isinstance(self.quantity, bool) or not isinstance(self.quantity, int):
            raise TypeError("quantity must be an integer")
        if self.quantity <= 0:
            raise InvalidOrderError("quantity must be greater than zero")

    @property
    def line_total(self) -> Money:
        """Return the total price for this line."""
        return self.unit_price.multiply(self.quantity)


@dataclass(frozen=True, slots=True)
class Order:
    """An order with a stable identifier and at least one item."""

    order_id: str
    customer_id: str
    customer_email: str
    items: tuple[OrderItem, ...]

    def __post_init__(self) -> None:
        if not self.order_id.strip():
            raise InvalidOrderError("order_id cannot be empty")
        if not self.customer_id.strip():
            raise InvalidOrderError("customer_id cannot be empty")
        if not self.customer_email.strip():
            raise InvalidOrderError("customer_email cannot be empty")
        normalized_items = tuple(self.items)
        if not normalized_items:
            raise InvalidOrderError("an order must contain at least one item")
        currencies = {item.unit_price.currency for item in normalized_items}
        if len(currencies) != 1:
            raise InvalidOrderError("all order items must use the same currency")
        object.__setattr__(self, "items", normalized_items)

    @property
    def subtotal(self) -> Money:
        """Calculate the sum of all line totals."""
        total = Money.zero(self.items[0].unit_price.currency)
        for item in self.items:
            total = total + item.line_total
        return total
