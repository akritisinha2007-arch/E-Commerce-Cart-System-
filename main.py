from product import Product
from cart_item import CartItem
from order import Order

products = []
products.append(Product(1, "Laptop", 55000, 5))
products.append(Product(2, "Headphones", 2000, 10))
products.append(Product(3, "Wireless Mouse", 800, 15))
products.append(Product(4, "Keyboard", 1500, 8))

cart = []
orders = []
wallet_balance = 60000


def show_products():
    if len(products) == 0:
        print("No products available.")
        return

    for product in products:
        print(product)


def find_product(id):
    for product in products:
        if product.id == id:
            return product
    return None


def add_to_cart():
    show_products()
    id = int(input("Enter Product ID to add: "))
    product = find_product(id)

    if product is None:
        print("Product not found.")
        return

    qty = int(input("Enter Quantity: "))

    if qty <= 0:
        print("Quantity must be more than 0.")
        return

    if qty > product.stock:
        print(f"Only {product.stock} left in stock.")
        return

    cart.append(CartItem(product, qty))
    print(f"{qty} x {product.name} added to cart.")


def show_cart():
    if len(cart) == 0:
        print("Your cart is empty.")
        return

    total = 0
    for item in cart:
        print(item)
        total += item.get_subtotal()

    print(f"Cart Total: Rs.{total}")


def get_cart_total():
    total = 0
    for item in cart:
        total += item.get_subtotal()
    return total


def checkout():
    global wallet_balance

    if len(cart) == 0:
        print("Cart is empty. Nothing to checkout.")
        return

    show_cart()
    total = get_cart_total()

    if total > wallet_balance:
        print("Insufficient wallet balance.")
        return

    confirm = input(f"Pay Rs.{total}? (yes/no): ")
    if confirm.lower() != "yes":
        print("Checkout cancelled.")
        return

    for item in cart:
        item.product.reduce_stock(item.quantity)

    wallet_balance -= total

    new_order = Order(cart.copy(), total)
    orders.append(new_order)
    cart.clear()

    print(f"Order placed successfully! Order ID: {new_order.id}")


def show_orders():
    if len(orders) == 0:
        print("No orders placed yet.")
        return

    for order in orders:
        print(order)


def cancel_order():
    global wallet_balance

    show_orders()
    if len(orders) == 0:
        return

    id = int(input("Enter Order ID to cancel: "))

    for order in orders:
        if order.id == id:
            cancelled = order.cancel()
            if cancelled:
                wallet_balance += order.total
                print(f"Order {id} cancelled. Rs.{order.total} refunded.")
            else:
                print(f"Order {id} is already {order.status}.")
            return

    print("Order not found.")


def show_wallet():
    print(f"Wallet Balance: Rs.{wallet_balance}")


while True:
    print("\n")
    print("===== SHOPPING CART SYSTEM =====")
    print("1. Show Products")
    print("2. Add to Cart")
    print("3. Show Cart")
    print("4. Checkout")
    print("5. Show Orders")
    print("6. Cancel Order")
    print("7. Show Wallet Balance")
    print("8. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        show_products()
    elif choice == "2":
        add_to_cart()
    elif choice == "3":
        show_cart()
    elif choice == "4":
        checkout()
    elif choice == "5":
        show_orders()
    elif choice == "6":
        cancel_order()
    elif choice == "7":
        show_wallet()
    elif choice == "8":
        print("Thank You")
        break
    else:
        print("Invalid Choice")

