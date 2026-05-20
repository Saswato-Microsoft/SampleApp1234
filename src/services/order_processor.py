"""Order processing service that orchestrates order validation, pricing, and fulfillment."""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from models.order import Order, OrderItem
from utils.discount_engine import (
    calculate_discounted_price,
    calculate_per_item_discount,
    calculate_savings_percentage,
    get_discount_percentage,
)


class OrderProcessor:
    """Processes customer orders through the pipeline."""

    def __init__(self):
        self.processed_orders = []
        self.failed_orders = []

    def validate_order(self, order):
        """Validate order has required fields.
        
        Bug: Does not validate that order has at least one item.
        Only checks for order_id and customer_id presence.
        """
        if not order.order_id:
            raise ValueError("Order must have an order_id")
        if not order.customer_id:
            raise ValueError("Order must have a customer_id")
        return True

    def apply_discount(self, order):
        """Apply discount code to the order.
        
        Bug: Calls calculate_per_item_discount without checking
        if the order has items, leading to ZeroDivisionError 
        propagating from discount_engine.py
        """
        if not order.discount_code:
            return order.get_total(), 0

        original_total = order.get_total()
        discounted_total = calculate_discounted_price(original_total, order.discount_code)
        total_discount = original_total - discounted_total

        # Bug: item_count will be 0 for empty orders
        item_count = order.get_item_count()
        per_item = calculate_per_item_discount(total_discount, item_count)

        return discounted_total, per_item

    def generate_receipt(self, order, discounted_total):
        """Generate receipt summary for the order.
        
        Bug: Calls calculate_savings_percentage which divides by
        original_total (0 for empty orders).
        """
        original_total = order.get_total()
        savings_pct = calculate_savings_percentage(original_total, discounted_total)

        return {
            "order_id": order.order_id,
            "customer_id": order.customer_id,
            "original_total": original_total,
            "final_total": discounted_total,
            "savings_percentage": savings_pct,
            "item_count": order.get_item_count(),
        }

    def process_order(self, order):
        """Full order processing pipeline.
        
        This is the main entry point. The bug manifests here when:
        - An order is created with no items (empty list)
        - But has a valid discount_code applied
        - validate_order() passes because it doesn't check items
        - apply_discount() crashes in discount_engine.calculate_per_item_discount()
        """
        try:
            self.validate_order(order)
            discounted_total, per_item_discount = self.apply_discount(order)
            receipt = self.generate_receipt(order, discounted_total)
            self.processed_orders.append(receipt)
            return receipt
        except Exception as e:
            self.failed_orders.append({"order_id": order.order_id, "error": str(e)})
            raise


if __name__ == "__main__":
    # This triggers the bug: empty order with a discount code
    empty_order = Order(
        order_id="ORD-2024-001",
        customer_id="CUST-500",
        items=[],  # No items!
        discount_code="SAVE20",  # But discount is applied
    )

    processor = OrderProcessor()
    result = processor.process_order(empty_order)
    print(result)
