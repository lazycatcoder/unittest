class Discount:
    def __init__(self, discount_rate):
        self.discount_rate = discount_rate
        self.discounted_categories = ['phone', 'laptop', 'tv']

    def apply_discount(self, price, category):
        if category in self.discounted_categories:
            return price * (1 - self.discount_rate)
        else:
            return price