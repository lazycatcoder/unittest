import unittest
from Lib.Cart import *


class TestCart(unittest.TestCase):
    def setUp(self):
        # Create product objects for testing
        self.item1 = Item('phone', 1000)
        self.item2 = Item('laptop', 1500)
        self.item3 = Item('tv', 2000)

        # Create an object of class Cart for testing
        self.cart = Cart()

    def test_add_item(self):
        # Add an item to the cart and check if it is in the list of items in the cart
        self.cart.add_item(self.item1)
        self.assertIn(self.item1, self.cart.get_items())

    def test_remove_item(self):
        # Add an item to the cart, then delete it and check if it is not in the list of items in the cart
        self.cart.add_item(self.item1)
        self.cart.remove_item(self.item1)
        self.assertNotIn(self.item1, self.cart.get_items())

    def test_get_total_price(self):
        # Add multiple items to the cart and check if the total cost is calculated correctly
        self.cart.add_item(self.item1)
        self.cart.add_item(self.item2)
        self.cart.add_item(self.item3)
        expected_total_price = self.item1.get_price() + self.item2.get_price() + self.item3.get_price()
        self.assertEqual(self.cart.get_total_price(), expected_total_price)

    def test_clear(self):
        # Add an item to the cart, then empty the cart and check if it's empty
        self.cart.add_item(self.item1)
        self.cart.clear()
        self.assertEqual(len(self.cart.get_items()), 0)


if __name__ == '__main__':
    unittest.main()