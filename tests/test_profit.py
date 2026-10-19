from decimal import Decimal

from main import minimum_pair_profit


def test_fees_can_eliminate_an_opportunity():
    profit = minimum_pair_profit(
        yes_cost=Decimal("0.55"),
        no_cost=Decimal("0.40"),
        total_fees=Decimal("0.06"),
    )

    assert profit == Decimal("-0.01")