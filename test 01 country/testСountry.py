import unittest
from Lib.Сountry import get_country


class TestLibraryСountry(unittest.TestCase):
    def test_allow_country(self):
        # Testing allowed countries
        iso_code_test_list = ['US', 'CA', 'UK', 'DE', 'JP', 'AU']
        for iso_code in iso_code_test_list:
            country = get_country(iso_code=iso_code)
            self.assertTrue(country[0]) # Check if the first element of the tuple is True
            self.assertEqual(dict, type(country[1])) # Check if the second element of the tuple is a dictionary

    def test_disallow_country(self):
        # Testing a banned country
        country = get_country(iso_code='BR')
        self.assertFalse(country[0]) # Check if the first element of the tuple is False
        self.assertEqual(None, country[1]) # Check if the second element of the tuple is None

    def test_raise_country_TypeError(self):
        # Testing for throwing a TypeError exception when the function is used incorrectly
        with self.assertRaises(TypeError):
            get_country() # Throw TypeError without passing arguments
            get_country(iso_code=12) # Throw a TypeError with a numeric argument

    def test_raise_country_ValueError(self):
        # Testing for throwing a ValueError exception when passing an invalid iso_code argument value
        with self.assertRaises(ValueError):
            get_country(iso_code='Japan') # Throw a ValueError with an invalid iso_code value
            get_country(iso_code='J') # Throw a ValueError with a short iso_code value
            get_country(iso_code='') # Throw a ValueError passing an empty string as the value of iso_code