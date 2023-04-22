# from django.db import transaction


class Transaction:
    def __init__(self):
        # Initialize account balance
        self.balance = 500  # Starting balance

    def execute_transaction(self, amount):
        try:
            # Creating a transaction context
            # with transaction.atomic():

            # Check if there are enough funds on the account
            if amount <= self.balance:
                # Execute a transaction - write off funds
                self.balance -= amount

                # Commit a transaction to the database
                # transaction.commit()

                return "Transaction successful"
            else:
                return "Insufficient funds"
        except Exception as e:
            # If an error occurs, rollback the transaction and display an error message
            # transaction.rollback()

            return "Error: {}".format(str(e))