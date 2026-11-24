"""A focused example of separating calculation from presentation."""

from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class InvoiceLine:
    description: str
    unit_price: Decimal
    quantity: int

    @property
    def total(self) -> Decimal:
        return self.unit_price * self.quantity


@dataclass(frozen=True)
class Invoice:
    lines: tuple[InvoiceLine, ...]

    @property
    def total(self) -> Decimal:
        return sum((line.total for line in self.lines), start=Decimal("0"))


def format_invoice(invoice: Invoice) -> str:
    """Format an invoice without owning its calculation rules."""
    rows = [f"{line.description}: {line.total:.2f}" for line in invoice.lines]
    rows.append(f"Total: {invoice.total:.2f}")
    return "\n".join(rows)


if __name__ == "__main__":
    sample = Invoice((InvoiceLine("Notebook", Decimal("4.50"), 2),))
    print(format_invoice(sample))
