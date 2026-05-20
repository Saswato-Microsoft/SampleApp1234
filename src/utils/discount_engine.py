"""Discount calculation engine for order processing."""

DISCOUNT_CODES = {
    "SAVE10": 10,
    "SAVE20": 20,
    "HALF50": 50,
    "LOYALTY": 15,
    "WELCOME": 25,
}


def get_discount_percentage(discount_code):
    """Retrieve discount percentage for a given code."""
    return DISCOUNT_CODES.get(discount_code, 0)


def calculate_discounted_price(original_price, discount_code):
    """Apply discount to original price and return final price."""
    discount_pct = get_discount_percentage(discount_code)
    discount_amount = original_price * (discount_pct / 100)
    return original_price - discount_amount


def calculate_per_item_discount(total_discount, item_count):
    """Distribute total discount evenly across items.
    
    Bug: Does not handle item_count=0, causing ZeroDivisionError
    when an order has no items but a discount code is applied.
    """
    per_item_share = total_discount / item_count  # ZeroDivisionError when item_count is 0
    return round(per_item_share, 2)


def calculate_savings_percentage(original_total, discounted_total):
    """Calculate how much percentage the customer saved.
    
    Bug: Does not handle original_total=0 (empty order scenario).
    """
    savings = original_total - discounted_total
    percentage_saved = (savings / original_total) * 100  # ZeroDivisionError when original_total is 0
    return round(percentage_saved, 2)
