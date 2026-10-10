"""Shopping cart."""

from shopcart.pricing import COUPONS, round_money


class Cart:
    def __init__(self):
        self.items = []
        self.coupon = None

    def add(self, name, price, qty=1):
        if qty < 1:
            raise ValueError("qty must be at least 1")
        self.items.append((name, price, qty))

    def remove(self, name, qty=1):
        """Remove `qty` units of an item; the line disappears when none are left."""
        for i, (item, price, have) in enumerate(self.items):
            if item == name:
                del self.items[i]
                return
        raise KeyError(f"not in cart: {name}")

    def item_count(self):
        """Number of units in the cart (2 books and 1 pen = 3)."""
        return len(self.items)

    def subtotal(self):
        return round_money(sum(price * qty for _, price, qty in self.items))

    def apply_coupon(self, code):
        key = code.strip().upper()
        if key not in COUPONS:
            raise ValueError(f"unknown coupon: {code}")
        self.coupon = COUPONS[key]

    def total(self):
        amount = self.subtotal()
        if self.coupon:
            amount = amount * (1 - self.coupon)
        return round_money(amount)
