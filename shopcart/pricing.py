"""Prices and coupons."""

COUPONS = {
    "SAVE10": 0.10,
    "SAVE25": 0.25,
}


def round_money(value: float) -> float:
    return round(value + 1e-9, 2)
