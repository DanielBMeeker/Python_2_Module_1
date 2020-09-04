"""
Program: test_user_account.py
Author: Daniel Meeker
Date: 9/3/2020

This file tests the user_account.py file
to make sure that the deposit and withdrawal
functions work as expected. I tested the
display function in the main file to get it
formatted in a way I liked.
"""
import unittest
from topic_9 import user_account as ua


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.user_account_1 = ua.UserAccount(1, 'checking')
        self.user_account_2 = ua.UserAccount(2, 'savings')

    def tearDown(self):
        del self.user_account_1, self.user_account_2

    def test_deposit(self):
        self.user_account_1.deposit(400)
        self.user_account_2.deposit(50)
        self.assertEqual(400, self.user_account_1.account_balance)
        self.assertEqual(50, self.user_account_2.account_balance)

    def test_withdrawal(self):
        self.user_account_1.deposit(400)
        self.user_account_1.withdrawal(250)
        self.assertEqual(150, self.user_account_1.account_balance)

    def test_withdrawal_error(self):
        with self.assertRaises(ValueError):
            self.user_account_2.deposit(50)
            self.user_account_2.withdrawal(100)


if __name__ == '__main__':
    unittest.main()
