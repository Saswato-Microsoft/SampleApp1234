"""Order model for the e-commerce processing pipeline."""


class OrderItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_subtotal(self):
        return self.price * self.quantity


class Order:
    def __init__(self, order_id, customer_id, items=None, discount_code=None):
        self.order_id = order_id
        self.customer_id = customer_id
        self.items = items if items is not None else []
        self.discount_code = discount_code
        self.status = "pending"

    def get_total(self):
        """Calculate order total from items."""
        return sum(item.get_subtotal() for item in self.items)

    def get_item_count(self):
        return len(self.items)
