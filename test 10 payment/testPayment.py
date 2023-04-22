import unittest
from unittest.mock import Mock, patch
from Lib.Payment import PaymentSystem


class TestPaymentSystem(unittest.TestCase):
    def test_make_payment_success(self):
        # Create a Mock for requests.post
        mock_post = Mock()
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {'status': 'success'}

        with patch('requests.post', mock_post):
            # Create an instance of PaymentSystem with mock api_key
            payment_system = PaymentSystem(api_key='test_api_key')
            
            # Call the make_payment method with test data
            result = payment_system.make_payment(amount=100)

            # Check that the request for the payment system API was completed with the correct arguments
            mock_post.assert_called_once_with(
                'https://api.paymentsystem.com/payments',
                headers={'Authorization': 'test_api_key'},
                json={'amount': 100}
            )

            # Check that the result of calling the make_payment method is equal to the expected value
            self.assertTrue(result)

    def test_make_payment_failure(self):
        # Create a mock for requests.post
        mock_post = Mock()
        mock_post.return_value.status_code = 500

        with patch('requests.post', mock_post):
            # Create an instance of PaymentSystem with mock api_key
            payment_system = PaymentSystem(api_key='test_api_key')
            
            # Call the make_payment method with test data
            result = payment_system.make_payment(amount=100)

            # Check that the request for the payment system API was completed with the correct arguments
            mock_post.assert_called_once_with(
                'https://api.paymentsystem.com/payments',
                headers={'Authorization': 'test_api_key'},
                json={'amount': 100}
            )

            # Check that the result of calling the make_payment method is equal to the expected value
            self.assertFalse(result)

    def test_check_payment_status_success(self):
        # Create a mock for requests.get
        mock_get = Mock()
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {'status': 'success'}

        with patch('requests.get', mock_get):
            # Create an instance of PaymentSystem with mock api_key
            payment_system = PaymentSystem(api_key='test_api_key')
            
            # Call the check_payment_status method with test data
            result = payment_system.check_payment_status(payment_id='test_payment_id')

           # Check that the request for the payment system API was completed with the correct arguments
            mock_get.assert_called_once_with(
                'https://api.paymentsystem.com/payments/test_payment_id',
                headers={'Authorization': 'test_api_key'}
            )

            # Check that the result of calling the check_payment_status method is equal to the expected value
            self.assertEqual(result, 'success')

    def test_check_payment_status_failure(self):
        # Create a mock for requests.get
        mock_get = Mock()
        mock_get.return_value.status_code = 404

        with patch('requests.get', mock_get):
            # Create an instance of PaymentSystem with mock api_key
            payment_system = PaymentSystem(api_key='test_api_key')
            
            # Call the check_payment_status method with test data
            result = payment_system.check_payment_status(payment_id='test_payment_id')

            # Check that the request for the payment system API was completed with the correct arguments
            mock_get.assert_called_once_with(
                'https://api.paymentsystem.com/payments/test_payment_id',
                headers={'Authorization': 'test_api_key'}
            )

            # Check that the result of calling the check_payment_status method is equal to the expected value
            self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()