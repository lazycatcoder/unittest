import unittest
from Lib.Auth import Auth


class AuthTest(unittest.TestCase):
    def setUp(self):
        # Create an instance of the class
        self.auth = Auth()

    def test_authenticate_valid_user(self):
        # test params
        login = "john_doe"
        password = "password123"
        uuid = "12345678-1234-5678-1234-567890abcdef"

        # Call authentication methods and implement tokens
        token = self.auth.authenticate(login, password, uuid)

        # Check if the token is not empty
        self.assertIsNotNone(token)        
        print("valid user")

    def test_authenticate_invalid_user(self):
        # test params
        login = "invalid_user"
        password = "invalid_password"
        uuid = "12345678-1234-5678-1234-567890abcdef"

        # Call the authentication method with invalid data and expect an error
        with self.assertRaises(Exception):
            self.auth.authenticate(login, password, uuid)
        print("invalid user")

    def test_access_purchase_page(self):
        # test params
        login = "john_doe"
        password = "password123"
        uuid = "12345678-1234-5678-1234-567890abcdef"

        # Call the authentication method and get the token
        token = self.auth.authenticate(login, password, uuid)

        # Call the method to check the availability of the product purchase page using the token
        result = self.auth.check_purchase_page_access(token)

        # Check if the page is available
        self.assertTrue(result)        
        print("access to the purchase page is allowed")

    def test_access_purchase_page_unauthorized(self):
        # test params
        token = "invalid_token"

       # Call the method to check the availability of the product purchase page with the wrong token and expect an error
        with self.assertRaises(Exception):
            self.auth.check_purchase_page_access(token)        
        print("access to the purchase page is denied")


if __name__ == '__main__':
    unittest.main()