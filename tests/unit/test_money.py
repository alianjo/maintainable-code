from decimal import Decimal

import pytest

from maintainable_shop.domain.exceptions import CurrencyMismatchError, DomainError
from maintainable_shop.domain.money import Money


def test_money_normalizes_currency_code() -> None:
    assert Money(Decimal("12.50"), "usd").currency == "USD"


def test_money_addition_returns_combined_amount() -> None:
    total = Money(Decimal("10.25"), "USD") + Money(Decimal("2.75"), "USD")
    assert total == Money(Decimal("13.00"), "USD")


def test_money_subtraction_returns_remaining_amount() -> None:
    remaining = Money(Decimal("15.00"), "USD") - Money(Decimal("4.25"), "USD")
    assert remaining == Money(Decimal("10.75"), "USD")


def test_money_rejects_mixed_currencies() -> None:
    with pytest.raises(CurrencyMismatchError):
        _ = Money(Decimal("10.00"), "USD") + Money(Decimal("5.00"), "EUR")


def test_money_rejects_negative_amount() -> None:
    with pytest.raises(DomainError, match="cannot be negative"):
        Money(Decimal("-0.01"), "USD")


def test_money_rejects_float_amounts() -> None:
    with pytest.raises(TypeError, match="Decimal"):
        Money(12.50, "USD")  # type: ignore[arg-type]


def test_money_cannot_be_subtracted_below_zero() -> None:
    with pytest.raises(DomainError, match="result cannot be negative"):
        _ = Money(Decimal("2.00"), "USD") - Money(Decimal("3.00"), "USD")


def test_money_multiply_requires_non_negative_integer() -> None:
    assert Money(Decimal("4.20"), "USD").multiply(3) == Money(Decimal("12.60"), "USD")
    with pytest.raises(DomainError):
        Money(Decimal("4.20"), "USD").multiply(-1)


def test_money_rejects_non_finite_amounts() -> None:
    with pytest.raises(DomainError, match="finite"):
        Money(Decimal("NaN"), "USD")


def test_money_rejects_invalid_currency_code() -> None:
    with pytest.raises(DomainError, match="three-letter"):
        Money(Decimal("1.00"), "US")


def test_money_multiply_rejects_boolean_quantity() -> None:
    with pytest.raises(TypeError, match="integer"):
        Money(Decimal("1.00"), "USD").multiply(True)
