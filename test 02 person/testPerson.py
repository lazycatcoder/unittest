import unittest
from Lib.Person import Person


class TestAllowedToBuyAlcohol(unittest.TestCase):
    def setUp(self):
        # Set up the test by creating a Person object
        self.__person = Person()

    def tearDown(self):
        # Clean up the test by deleting the Person object
        del self.__person

    def test_age_are_too_low_to_buy(self):
        # Test case to check if a person with age below the legal limit cannot buy alcohol
        result = self.__person.allowed_to_buy_alcohol('2008-01-01', 4.6)
        self.assertFalse(result)
        print("Test result: Sale is not allowed. (age: too low)")

    def test_age_is_allowed_to_buy(self):
        # Test case to check if a person with age above the legal limit can buy alcohol
        result = self.__person.allowed_to_buy_alcohol('1980-01-01', 46.6)
        self.assertTrue(result)
        print("Test result: Sale is allowed. (age: allowed)")

    def test_age_is_allowed_to_buy_tobacco(self):
        # Test case to check if a person with age above the legal limit can buy tobacco
        result = self.__person.allowed_to_buy_tobacco('2000-01-01')
        self.assertTrue(result)
        print("Test result: Sale is allowed. (age: allowed)")

    def test_age_is_not_allowed_to_buy_tobacco(self):
        # Test case to check if a person with age below the legal limit cannot buy tobacco
        result = self.__person.allowed_to_buy_tobacco('2015-01-01')
        self.assertFalse(result)
        print("Test result: Sale is not allowed. (age: too low)")


if __name__ == '__main__':
    unittest.main()