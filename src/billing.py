"""Billing module that calculates final prices with tax."""

from tax_config import get_tax_rate


def calculate_total_with_tax(price, region):
    """Calculate the final price including tax for a given region.
    
    Bug: Uses addition (price + tax_rate) instead of the correct
    percentage formula: price * (1 + tax_rate / 100).
    
    This also crashes with TypeError because get_tax_rate() returns
    a string, and you cannot add a float (price) to a string.
    
    Fix: Change formula to price * (1 + tax_rate / 100).
    """
    tax_rate = get_tax_rate(region)
    total = price + tax_rate  # Bug: wrong formula AND type mismatch
    return round(total, 2)


def generate_invoice(items, region):
    """Generate an invoice with tax applied to each item.
    
    Entry point that triggers the bug.
    """
    invoice_lines = []
    for item in items:
        name = item["name"]
        price = item["price"]
        total = calculate_total_with_tax(price, region)
        invoice_lines.append({"item": name, "price": price, "total_with_tax": total})

    return invoice_lines


if __name__ == "__main__":
    # Triggers TypeError: unsupported operand type(s) for +: 'float' and 'str'
    order_items = [
        {"name": "Laptop", "price": 999.99},
        {"name": "Mouse", "price": 29.99},
    ]
    invoice = generate_invoice(order_items, "IN")
    print(invoice)
