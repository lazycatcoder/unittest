import unittest
from datetime import date
from unittest.mock import patch
from Lib.CodeGenerator import CodeGenerator


class CodeGeneratorTest(unittest.TestCase):
    def setUp(self):
        self.generator = CodeGenerator()

    def test_generate_random_code(self):
        code = self.generator.generate_random_code(16)
        self.assertEqual(len(code), 16)

    def test_generate_code_from_date(self):
        # Get the current date
        current_date = date.today()
        code = self.generator.generate_code_from_date()
        # Expected result is a string with the format '%y%m%d' of the current date
        expected_code = current_date.strftime('%y%m%d')
        self.assertEqual(code, expected_code)

    def test_generate_code_with_country_prefix(self):
        # with - context for creating mock objects
        # Mock objects replace the corresponding generate_random_code() and generate_code_from_date() methods of the code_generator object
        with patch.object(self.generator, 'generate_random_code') as mock_generate_random_code, \
                patch.object(self.generator, 'generate_code_from_date') as mock_generate_code_from_date:
            
            # Set return values for mock objects
            mock_generate_random_code.return_value = 'ABCDEFGHIJKL1234'
            mock_generate_code_from_date.return_value = date.today().strftime('%y%m%d')
           
            # Calls the generate_code_with_country_prefix() method on the code_generator object with the "United States" argument and stores the result in the code variable
            code = self.generator.generate_code_with_country_prefix("United States")
           
            self.assertEqual(len(code), 26)
            self.assertTrue(code.startswith("US-"))

        # check when calling the generate_code_with_country_prefix() method with the argument "Invalid Country" a ValueError exception is raised
        with self.assertRaises(ValueError): 
            self.generator.generate_code_with_country_prefix("Invalid Country")


if __name__ == "__main__":
    unittest.main()