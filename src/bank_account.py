# bank_account.py
"""
Problem Description:
Create a BankAccount class that models a simple banking system. This class should support the following functionality:
1. __init__(self, account_holder: str, initial_balance: float):
Initializes an account with the name of the account holder and an initial balance. The balance cannot be negative.
2. deposit(self, amount: float):
Deposits the specified amount into the account. If the amount is less than or equal to zero, it raises a ValueError.
3. withdraw(self, amount: float):
Withdraws the specified amount from the account. If the withdrawal amount exceeds the available balance, it raises an InsufficientFundsError (which should be defined as a custom exception).
If the amount is less than or equal to zero, it raises a ValueError.
4. get_balance(self):
Returns the current balance of the account.
5. transfer(self, recipient_account, amount: float):
Transfers the specified amount to another BankAccount instance. If the amount exceeds the balance or is less than or equal to zero, it raises an InsufficientFundsError or ValueError, respectively.
6. __str__(self):
Returns a string representation of the account in the format: AccountHolder: {account_holder_name}, Balance: {current_balance}.

Custom Exception:
Define a custom exception InsufficientFundsError that will be raised when an account has insufficient funds for a withdrawal or transfer.
"""

class InsufficientFundsError(Exception):
    pass

class BankAccount:
    def __init__(self, account_holder: str, initial_balance: float):
        # Initialize the bank account
        pass

    def deposit(self, amount: float):
        # Deposit amount to the account
        pass

    def withdraw(self, amount: float):
        # Withdraw amount from the account
        pass

    def get_balance(self):
        # Return current account balance
        pass

    def transfer(self, recipient_account, amount: float):
        # Transfer amount to another account
        pass

    def __str__(self):
        # Return the string representation of the account
        pass