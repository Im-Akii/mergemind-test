from shopcart.cart import Cart


def test_subtotal_and_total():
    cart = Cart()
    cart.add("book", 12.50, qty=2)
    cart.add("pen", 1.25)
    assert cart.subtotal() == 26.25
    assert cart.total() == 26.25


def test_coupon_discount():
    cart = Cart()
    cart.add("book", 100.0)
    cart.apply_coupon("SAVE10")
    assert cart.total() == 90.0
