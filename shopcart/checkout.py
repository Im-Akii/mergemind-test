"""Order total: cart total (after any coupon) + sales tax + shipping."""

from shopcart.pricing import round_money
from shopcart.shipping import shipping_fee

TAX_RATES = {"CA": 0.0725, "NY": 0.04, "OR": 0.0}


def sales_tax(cart, region: str) -> float:
    """Sales tax on what the customer actually pays for the goods."""
    rate = TAX_RATES.get(region)
    if rate is None:
        raise ValueError(f"unknown region: {region}")
    return round_money(cart.subtotal() * rate)


def order_total(cart, region: str) -> float:
    goods = cart.total()
    return round_money(goods + sales_tax(cart, region) + shipping_fee(goods))
