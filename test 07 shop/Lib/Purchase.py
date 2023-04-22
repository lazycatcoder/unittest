from Lib.Product import *


class Purchase:
    # Method for placing an order
    @staticmethod
    def place_order(product, quantity, payment_method):
        # Checking if the product has already applied a discount, then it is not allowed to apply a discount by a promotional code
        if product.discount_applied:
            raise ValueError("Product discount has already been applied, the use of a promotional code is not allowed")
        
        total_price = product.calculate_total_price(quantity)

        # Check available payment methods
        if payment_method not in ['cash', 'credit_card']:
            raise ValueError("Invalid payment method")
        
        # If the payment method is 'cash', then add 10% commission
        if payment_method == 'cash':
            total_price *= 1.1

        # Placing an order and returning the total amount of the order
        return total_price
    

    # Method for applying discount by promo code
    @staticmethod
    def apply_discount_by_promocode(product, quantity, promocode):
        # Calculation of the total cost of the goods
        total_price = product.calculate_total_price(quantity)

       # Checking if the product has already applied a discount, then it is not allowed to apply a discount by a promotional code
        if product.discount_applied:
            raise ValueError("Product discount already applied, promo code cannot be used")
        
        # Checking the promotional code and applying the discount
        if promocode == 'DISCOUNT10':
            discount = total_price * 0.1
            total_price -= discount
            product.discount_applied = True

        # Return the total discounted amount
        return total_price