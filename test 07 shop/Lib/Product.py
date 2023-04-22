class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
        self.discount_applied = False

    # Method for calculating the amount of goods, taking into account the quantity
    def calculate_total_price(self, quantity):
        return self.price * quantity

    # Method for calculating the amount of goods including tax 20%
    def calculate_total_price_with_vat(self, quantity):
        total_price = self.price * quantity
        vat = total_price * 0.2
        return total_price + vat

    # Method for calculating the amount of goods, taking into account a 10% discount
    def calculate_total_price_with_discount(self, quantity):
        total_price = self.price * quantity
        discount = total_price * 0.1
        return total_price - discount