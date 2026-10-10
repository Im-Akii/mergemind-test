# shopcart (MergeMind sandbox)

A tiny shopping cart used to test MergeMind end to end.

    from shopcart.cart import Cart
    cart = Cart()
    cart.add("book", 100.0)
    cart.apply_coupon("SAVE10")
    cart.total()  # 90.0

Run the tests with `python -m pytest`.
