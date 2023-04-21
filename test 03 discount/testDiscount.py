import unittest
from Lib.Discount import Discount


class TestDiscount(unittest.TestCase):
    def test_discounted_categories(self):
        # Create an object of class Discount with different discount values
        discount = Discount(0.10) # 10% discount
        discount_2 = Discount(0.18) # 18% discount
        discount_3 = Discount(0.30) # 30% discount

        # Testing the discount applied to the 'phone' category
        price = 1000
        category = 'phone'
        expected_price = round(price * (1 - 0.10), 2)
        self.assertAlmostEqual(discount.apply_discount(price, category), expected_price, delta=0.01)

        # Testing the discount applied to the 'laptop' category
        price = 1500
        category = 'laptop'
        expected_price = round(price * (1 - 0.18), 2)
        self.assertAlmostEqual(discount_2.apply_discount(price, category), expected_price, delta=0.01)

        # Testing the discount applied to the 'tv' category
        price = 2000
        category = 'tv'
        expected_price = round(price * (1 - 0.30), 2)
        self.assertAlmostEqual(discount_3.apply_discount(price, category), expected_price, delta=0.01)


if __name__ == '__main__':
    unittest.main()