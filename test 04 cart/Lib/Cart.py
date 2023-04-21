class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price


class Cart:
    def __init__(self):
        self.items = []  # List to store items in the cart

    def add_item(self, item):
        self.items.append(item)  # Add an item to the cart

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)  # Remove an item from the cart if it exists

    def get_items(self):
        return self.items  # Return the list of items in the cart

    def clear(self):
        self.items = []  # Clear all items from the cart

    def get_total_price(self):
        total_price = 0
        for item in self.items:
            total_price += item.get_price()  # Calculate the total price of all items in the cart
        return total_price  # Return the total price
