class Order:

    order_count = 1

    def __init__(self, items, total):
        self.id = Order.order_count
        Order.order_count += 1
        self.items = items
        self.total = total
        self.status = "Placed"

    def cancel(self):
        if self.status == "Placed":
            self.status = "Cancelled"
            return True
        else:
            return False

    def __str__(self):
        item_lines = ", ".join(str(item) for item in self.items)
        return (f"Order ID: {self.id} | "
                f"Items: {item_lines} | "
                f"Total: Rs.{self.total} | "
                f"Status: {self.status}")

