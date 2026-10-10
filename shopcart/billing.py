"""Invoice reconciliation (unrelated to carts)."""


def reconcile(entries):
    outstanding = sum(e["amount"] for e in entries if not e.get("settled"))
    return round(outstanding, 2)
