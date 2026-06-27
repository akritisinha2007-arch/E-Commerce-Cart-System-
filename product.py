class Product:

    def __init__(self, id, name, price, stock):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock

    def reduce_stock(self, qty):
        if qty <= self.stock:
            self.stock -= qty
            return True
        else:
            return False

    def __str__(self):
        return (f"ID: {self.id} | "
                f"Name: {self.name} | "
                f"Price: Rs.{self.price} | "
                f"Stock: {self.stock}")
