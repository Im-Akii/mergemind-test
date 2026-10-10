import pytest

from shopcart.cart import Cart
from shopcart.checkout import order_total, sales_tax
from shopcart.shipping import shipping_fee


def test_shipping_fee():
    assert shipping_fee(20.0) == 4.99
    assert shipping_fee(80.0) == 0.0


def test_order_total_without_coupon():
    cart = Cart()
    cart.add("book", 15.0, qty=2)
    assert sales_tax(cart, "NY") == 1.2
    assert order_total(cart, "NY") == 36.19  # 30.00 + 1.20 tax + 4.99 shipping


def test_tax_free_region():
    cart = Cart()
    cart.add("lamp", 120.0)
    assert order_total(cart, "OR") == 120.0


def test_unknown_region():
    cart = Cart()
    cart.add("pen", 1.0)
    with pytest.raises(ValueError, match="unknown region"):
        sales_tax(cart, "XX")


def test_remove_single_item_and_count():
    cart = Cart()
    cart.add("book", 10.0)
    cart.add("pen", 1.0)
    assert cart.item_count() == 2
    cart.remove("pen")
    assert cart.item_count() == 1
    with pytest.raises(KeyError):
        cart.remove("pen")
