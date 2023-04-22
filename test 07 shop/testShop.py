import unittest
from parameterized import parameterized
from Lib.Purchase import Purchase
from Lib.Product import Product


class TestProductPurchase(unittest.TestCase):
    # Method for setting test data
    def setUp(self):
        # Create products for each category
        self.laptops = [Product("Laptop1", 1000, "laptops"),
                        Product("Laptop2", 1500, "laptops"),
                        Product("Laptop3", 1200, "laptops")]

        self.phones = [Product("Phone1", 800, "phones"),
                       Product("Phone2", 900, "phones"),
                       Product("Phone3", 1000, "phones")]
    
    # Method for testing checkout
    def test_place_order(self):
        # Create a product object
        product = Product("Laptop1", 1000, "laptops")
        # Call the method under test
        total_price = Purchase.place_order(product, 2, 'cash')
        # Check result
        self.assertEqual(total_price, 2200)  # Changed expected result to 2200
        # Checking that the product discount has not been applied
        self.assertFalse(product.discount_applied)

    # Method for testing the calculation of the amount of goods, taking into account the quantity
    def test_calculate_total_price(self):
        # Create a product object
        product = Product("Laptop1", 1000, "laptops")
        # Call the method under test
        total_price = product.calculate_total_price(2)
        # Check result
        self.assertEqual(total_price, 2000)

    # Method for testing the calculation of the amount of goods, taking into account a 10% discount
    def test_calculate_total_price_with_discount(self):
        # Checking the calculation of the amount, taking into account the discount for each category of goods
        for product in self.laptops:
            total_price = product.calculate_total_price_with_discount(2)
            self.assertEqual(total_price, 1800)

        for product in self.phones:
            total_price = product.calculate_total_price_with_discount(3)
            self.assertEqual(total_price, 1680)

    # Method for testing the application of a promo code discount
    def test_apply_discount_by_promocode(self):
        # Create a product object
        product = Product("Laptop1", 1000, "laptops")
        # Call the method under test
        total_price = Purchase.apply_discount_by_promocode(product, 2, 'DISCOUNT10')
        # Check result
        self.assertEqual(total_price, 1800)

        # Check that the promo code discount cannot be applied again if there is already a discount on the product
        product_with_discount = Product("Laptop2", 1500, "laptops")
        Purchase.apply_discount_by_promocode(product_with_discount, 1, 'DISCOUNT10')
        with self.assertRaises(ValueError):
            Purchase.apply_discount_by_promocode(product_with_discount, 1, 'DISCOUNT10')

    # Method for testing the calculation of the amount of goods, taking into account a 10% discount
    def test_calculate_total_price_with_discount(self):
        # Create a product object
        product = Product("Laptop1", 1000, "laptops")
        # Call the method under test, passing the quantity argument
        total_price = product.calculate_total_price_with_discount(2)
        # Check result
        self.assertEqual(total_price, 1800)

    # Method to test place_order method with wrong payment method
    def test_place_order_with_wrong_payment_method(self):
        # Create a product object
        product = Product("Laptop1", 1000, "laptops")
        # Check for an error with an incorrect payment method
        with self.assertRaises(ValueError):
            Purchase.place_order(product, 2, 'paypal')

    # Method for testing the calculation of the amount of the goods, taking into account the tax of 20%
    def test_calculate_total_price_with_vat(self):
        # Checking the calculation of the amount including tax for each category of goods
        for product in self.laptops + self.phones:
            # Call the method under test
            total_price_with_vat = product.calculate_total_price_with_vat(2)
            # Expected Result
            expected_total_price_with_vat = product.price * 2 * 1.2
            # Check result
            self.assertEqual(total_price_with_vat, expected_total_price_with_vat)

    # Testing the place_order method using parameterization
    @parameterized.expand([
        # Test data: product, quantity, payment_method, expected_total_price
        (Product("Phone1", 1000, "phones"), 2, "cash", 2200),
        (Product("Laptop1", 2000, "laptops"), 3, "credit_card", 6000),
        (Product("Phone2", 1000, "phones"), 1, "cash", 1100)
    ])
    def test_place_order_with_parameterization(self, product, quantity, payment_method, expected_total_price):
        # Call the method under test
        total_price = Purchase.place_order(product, quantity, payment_method)
        
        # Round expected and actual amount to 2 decimal places
        expected_total_price = round(expected_total_price, 2)
        total_price = round(total_price, 2)

        # Check for equality of expected and actual amount
        self.assertEqual(total_price, expected_total_price)

    # Testing the apply_discount_by_promocode method using parameterization
    @parameterized.expand([
        # Test data: product, quantity, promocode, expected_total_price
        (Product("Phone1", 1000, "phones"), 2, "DISCOUNT10", 1800),
        (Product("Laptop1", 2000, "laptops"), 3, "DISCOUNT10", 5400),
        (Product("Phone2", 1500, "phones"), 1, "DISCOUNT10", 1350)
    ])
    def test_apply_discount_by_promocode_with_parameterization(self, product, quantity, promocode, expected_total_price):
        # Call the method under test
        total_price = Purchase.apply_discount_by_promocode(product, quantity, promocode)
        # Checking if the expected value matches
        self.assertEqual(total_price, expected_total_price)

# Create a test suite
# def suite():
#     suite = unittest.TestSuite()
#     suite.addTest(TestProductPurchase("test_place_order"))
#     suite.addTest(TestProductPurchase("test_apply_discount_by_promocode"))
#     suite.addTest(TestProductPurchase("test_calculate_total_price_with_discount"))
#     suite.addTest(TestProductPurchase("test_calculate_total_price_with_vat"))
#     suite.addTest(TestProductPurchase("test_calculate_total_price_with_quantity"))
#     suite.addTest(TestProductPurchase("test_place_order_with_wrong_payment_method"))
#     return suite


if __name__ == '__main__':
    unittest.main()
    # runner = unittest.TextTestRunner()
    # runner.run(suite())