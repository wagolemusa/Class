import unittest

from bank_account import *

class AccountBalanceTestCase(unittest.TestCase):
	def setUp(self):
		self.account_yangu = BankAccount()

	# test for account 
	def test_balance(self):
		self.assertEqual(self.account_yangu.balance, 3000, msg='Account Balance Invalid.')

	# test for deposting account
	def test_deposit(self):
		self.account_yangu.deposit(4000)
		self.assertEqual(self.account_yangu.balance, 7000, msg='Depost Method Inaccurate.')

	# test for withdrawing 
	def test_withdraw(self):
		self.account_yangu.withdraw(500)
		self.assertEqual(self.account_yangu.balance, 2500, msg='Withdraw method Inaccurate.')

	# test for If amount is greater than the balance return
	def test_invalid_transaction(self):
		self.assertEqual(self.account_yangu.withdraw(6000), "Invalid Transaction", msg='Invalid Transction.')
	
	 # test for sub classes
	def test_sub_class(self):
		self.assertTrue(issubclass(MinimumBalanceAccount, BankAccount), msg='Not True subclass of Balance Account.')


if __name__ == '__main__':
	unittest.main()
