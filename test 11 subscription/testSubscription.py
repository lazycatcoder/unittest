import unittest
from unittest.mock import patch
from Lib.Subscription import *


class TestStreamingService(unittest.TestCase):
    def setUp(self):
        self.streaming_service = StreamingService()

    def test_purchase_subscription_with_credit_card(self):
        payment_amount = 10
        subscription_type = 'basic'
        payment_method = 'credit_card'
        expected_status = payment_amount // self.streaming_service.subscriptions[subscription_type]

        # Patch the 'process_card_payment' method of the BankPaymentSystem
        with patch.object(BankPaymentSystem, 'process_card_payment') as mock_process_card_payment:
            # Call the method being tested
            self.assertEqual(self.streaming_service.purchase_subscription(subscription_type, payment_method, payment_amount), expected_status)
            # Assert that the 'process_card_payment' method was called once with the expected payment amount
            mock_process_card_payment.assert_called_once_with(payment_amount)

    def test_purchase_subscription_with_third_part(self):
        payment_amount = 45
        subscription_type = 'premium'
        payment_method = 'third_part'
        expected_status = payment_amount // self.streaming_service.subscriptions[subscription_type]

        # Patch the 'process_payment' method of the ThirdPartPaymentSystem
        with patch.object(ThirdPartPaymentSystem, 'process_payment') as mock_process_payment:
            # Call the method being tested
            self.assertEqual(self.streaming_service.purchase_subscription(subscription_type, payment_method, payment_amount), expected_status)
            # Assert that the 'process_payment' method was called once with the expected payment amount
            mock_process_payment.assert_called_once_with(payment_amount)

    def test_purchase_subscription_with_wrong_payment_method(self):
        payment_amount = 10
        subscription_type = 'standard'
        payment_method = 'invalid_method'

        # Assert that calling the method with an invalid payment method raises a ValueError
        with self.assertRaises(ValueError):
            self.streaming_service.purchase_subscription(subscription_type, payment_method, payment_amount)

    def test_purchase_subscription_with_wrong_subscription_type(self):
        payment_amount = 10
        subscription_type = 'invalid_subscription_type'
        payment_method = 'credit_card'

        # Assert that calling the method with an invalid subscription type raises a ValueError
        with self.assertRaises(ValueError):
            self.streaming_service.purchase_subscription(subscription_type, payment_method, payment_amount)

    def test_check_subscription_status(self):
        subscription_type = 'standard'
        expected_status = 2
        self.streaming_service.subscriptions_status[subscription_type] = expected_status

        # Call the method being tested and assert that the returned status matches the expected status
        self.assertEqual(self.streaming_service.check_subscription_status(subscription_type), expected_status)

    def test_check_subscription_status_with_invalid_subscription_type(self):
        subscription_type = 'invalid_subscription_type'

        # Assert that calling the method with an invalid subscription type raises a ValueError
        with self.assertRaises(ValueError):
            self.streaming_service.check_subscription_status(subscription_type)

    def test_check_subscription_status_with_subscription_not_found(self):
        subscription_type = 'premium'

        # Assert that calling the method with a subscription type that is not found raises a ValueError
        with self.assertRaises(ValueError):
            self.streaming_service.check_subscription_status(subscription_type)


if __name__ == '__main__':
    unittest.main()