"""
Program: user_account.py
Author: Daniel Meeker
Date: 9/3/2020

This program will utilize a class to create
a UserAccount object which will allow the
user to either deposit, withdraw, or display
their account balance.
"""


class UserAccount:
    """
    User Account class
    """

    def __init__(self, account_number, account_type, account_balance=0):
        """
        class constructor
        :param account_number: required
        :param account_type: required
        :param account_balance: optional
        """
        self.account_number = account_number
        self.account_type = account_type
        self.account_balance = account_balance

    def deposit(self, credit):
        self.account_balance += credit

    def withdrawal(self, debit):
        if self.account_balance < debit:
            raise ValueError("Your account does not have enough money to complete this transaction.")
        self.account_balance -= debit

    def display(self):
        return ("Account " + str(self.account_number) + " is a " + str(self.account_type)
                + " account and has a balance of $" + str(f'{self.account_balance:.2f}'))


if __name__ == '__main__':
    account1 = UserAccount(1, 'checking')
    account1.deposit(400)
    print(account1.display())
    account1.withdrawal(250)
    print(account1.display())
    try:
        account2 = UserAccount(2, "savings")
        account2.deposit(50)
        print(account2.display())
        account2.withdrawal(100)
        print(account2.display())
    except ValueError as e:
        print(e)
    del account1, account2
