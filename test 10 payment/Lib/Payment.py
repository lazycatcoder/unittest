import requests


class PaymentSystem:
    def __init__(self, api_key):
        self.api_key = api_key

    def make_payment(self, amount):
        # Sending a request to the payment system API to make a payment
        response = requests.post(
            f'https://api.paymentsystem.com/payments',
            headers={'Authorization': self.api_key},
            json={'amount': amount}
        )
        if response.status_code == 200:
            return True
        else:
            return False

    def check_payment_status(self, payment_id):
        # Sending a request to the payment system API to check the payment status
        response = requests.get(
            f'https://api.paymentsystem.com/payments/{payment_id}',
            headers={'Authorization': self.api_key}
        )
        if response.status_code == 200:
            return response.json()['status']
        else:
            return None