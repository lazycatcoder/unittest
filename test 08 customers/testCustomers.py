import sqlite3
import unittest
from Lib.Customers import Customers


class CustomersTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Create a temporary database for testing
        cls.connection = sqlite3.connect('Lib\customers.db')
        cls.cursor = cls.connection.cursor()
        cls.cursor.execute('''
            CREATE TABLE IF NOT EXISTS customers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT,
                last_name TEXT,
                email TEXT,
                phone TEXT,
                country TEXT
            )
        ''')
        cls.connection.commit()
        cls.customers = Customers()

    @classmethod
    def tearDownClass(cls):
        # Closing the database connection and deleting the temporary database
        cls.cursor.close()
        cls.connection.close()

    def test_add_customer(self):
        # Adding 5 users for testing
        self.customers.add_customer("John", "Doe", "john.doe@example.com", "1234567890", "USA")
        self.customers.add_customer("Jane", "Smith", "jane.smith@example.com", "9876543210", "Canada")
        self.customers.add_customer("Michael", "Brown", "michael.brown@example.com", "5555555555", "USA")
        self.customers.add_customer("Emma", "Johnson", "emma.johnson@example.com", "7777777777", "Canada")
        self.customers.add_customer("David", "Lee", "david.lee@example.com", "9999999999", "USA")

        # Checking the add_customer() method to add a user
        self.cursor.execute("SELECT COUNT(*) FROM customers")
        result = self.cursor.fetchone()[0]
        self.assertEqual(result, 5, "Customers not added successfully")

    def test_find_customers_by_name(self):
        # Check the find_customers_by_name() method to find users by name
        expected_output = [(1, 'John', 'Doe', 'john.doe@example.com', '1234567890', 'USA')]
        actual_output = self.customers.find_customers_by_name("John", "Doe")
        self.assertEqual(expected_output, actual_output)

    def test_find_customers_by_country(self):
        # Check the find_customers_by_country() method to find users by country
        expected_output = [(2, 'Jane', 'Smith', 'jane.smith@example.com', '9876543210', 'Canada'), (4, 'Emma', 'Johnson', 'emma.johnson@example.com', '7777777777', 'Canada')]
        actual_output = self.customers.find_customers_by_country("Canada")
        expected_output_list = sorted(expected_output)
        actual_output_list = sorted(actual_output)
        self.assertListEqual(expected_output_list, actual_output_list)


if __name__ == '__main__':
    unittest.main()