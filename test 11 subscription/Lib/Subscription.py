import requests


class StreamingService:
    def __init__(self):
        self.subscriptions = {'basic': 5, 'standard': 10, 'premium': 15}  # Define subscription types and their costs
        self.payment_methods = ['credit_card', 'debit_card', 'third_part']  # Define supported payment methods
        self.subscriptions_status = {}  # Store subscription status

    def purchase_subscription(self, subscription_type, payment_method, payment_amount):
        if subscription_type not in self.subscriptions.keys():  # Check if subscription type is supported
            raise ValueError('Unsupported subscription')
        
        if payment_method == 'credit_card':
            bank_payment_system = BankPaymentSystem(card_number='1234567890', username='user123', password='password123')
            bank_payment_system.process_card_payment(payment_amount)  # Process payment using bank payment system
        elif payment_method == 'third_part':
            third_part_payment_system = ThirdPartPaymentSystem(api_key='api_key123')
            third_part_payment_system.process_payment(payment_amount)  # Process payment using third-party payment system
        else:
            raise ValueError('Unsupported payment method')  # Raise error for unsupported payment method

        subscription_cost = self.subscriptions[subscription_type]  # Get subscription cost for the given type
        self.subscriptions_status[subscription_type] = payment_amount // subscription_cost  # Update subscription status
        return self.subscriptions_status[subscription_type]  # Return updated subscription status

    def check_subscription_status(self, subscription_type):
        if subscription_type not in self.subscriptions.keys():  # Check if subscription type is supported
            raise ValueError('Unsupported subscription')
        if subscription_type not in self.subscriptions_status.keys():  # Check if subscription status is available
            raise ValueError('Subscription not found')
        return self.subscriptions_status[subscription_type]  # Return subscription status


class BankPaymentSystem:
    def __init__(self, card_number, username, password):
        self.card_number = card_number
        self.username = username
        self.password = password

    def __authenticate_user(self):
        # Authenticates the user with the bank API
        payload = {
            'username': self.username,
            'password': self.password
        }
        response = requests.post('https://bank-api.com/authenticate_user', json=payload)
        if response.status_code == 200:
            auth_token = response.json().get('auth_token')
            return auth_token
        else:
            raise Exception('User authentication error')

    def __check_card_balance(self, amount):
        # Checks if the card has sufficient balance for the payment
        auth_token = self.__authenticate_user()
        response = requests.get(f'https://bank-api.com/check_balance?card_number={self.card_number}', 
                                headers={'Authorization': f'Bearer {auth_token}'})
        if response.status_code == 200:
            card_balance = response.json().get('balance', 0)
            return card_balance >= amount
        else:
            raise Exception('Error when checking card balance')

    def __debit_card(self, amount, auth_token):
        # Debits the card with the payment amount
        payload = {
            'card_number': self.card_number,
            'amount': amount
        }
        response = requests.post('https://bank-api.com/debit_card', 
                                json=payload, 
                                headers={'Authorization': f'Bearer {auth_token}'})
        if response.status_code != 200:
            raise Exception('Error when debiting funds from the card')

    def process_card_payment(self, amount):
        # Processes the payment using a bank card
        auth_token = self.__authenticate_user()
        if self.__check_card_balance(amount):
            try:
                self.__debit_card(amount, auth_token)
                print(f'Payment for the amount {amount}$ using a bank card was successful')
            except Exception as e:
                print(f'Error when debiting funds from the card: {e}')
        else:
            raise ValueError('Insufficient funds on the card to complete the payment')


class ThirdPartPaymentSystem:
    def __init__(self, api_key):
        self.api_key = api_key

    # Private method to authenticate the API key
    def __authenticate_api_key(self):
        response = requests.post('https://third-part-payment.com/authenticate_api_key', 
                                json={'api_key': self.api_key})
        if response.status_code == 200:
            auth_token = response.json().get('auth_token')
            return auth_token
        else:
            raise Exception('Error authenticating API key')

    # Private method to process the payment
    def __process_payment(self, amount):
        auth_token = self.__authenticate_api_key()
        payload = {
            'amount': amount,
            'api_key': self.api_key
        }
        # Make a post request to the payment processing API with the payment details and the authorization token
        response = requests.post('https://third-part-payment.com/process_payment', 
                                json=payload, 
                                headers={'Authorization': f'Bearer {auth_token}'})
        # If the payment is successful, print a success message
        if response.status_code == 200:
            print(f'Payment for the amount {amount}$ using a third-party service was successful')
        # Otherwise, raise an exception
        else:
            raise Exception('Error making payment through a third party service')

    # Public method to process the payment with error handling
    def process_payment(self, amount):
        try:
            self.__process_payment(amount)
        # Catch any exceptions that may occur during payment processing and print an error message
        except Exception as e:
            print(f'Error making payment via third party service: {e}')