import unittest
from Lib.Transaction import Transaction


class TransactionTest(unittest.TestCase):
    def test_transaction_success(self):
        # Create an instance of the Transaction class
        transaction = Transaction()
        # Execute transaction
        result = transaction.execute_transaction(100)  # pass the transaction amount
        # Check if the transaction was successful
        self.assertEqual(result, "Transaction successful")

    def test_transaction_insufficient_funds(self):
        # Create an instance of the Transaction class
        transaction = Transaction()
        # Execute a transaction with insufficient funds on the account
        result = transaction.execute_transaction(1000)  # Pass the transaction amount
        # Check if the transaction failed due to lack of funds
        self.assertEqual(result, "Insufficient funds")


if __name__ == '__main__':
    unittest.main()