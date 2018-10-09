import unittest
from unittest.mock import patch
from employ import Employee

class TestEmployee(unittest.TestCase):


	@classmethod
	def setUpClass(cls):
		print('setUpClass')

	@classmethod	
	def tearDownClass(cls):
		print('teardownClass')


	def setUp(self):
		self.emp_1 = Employee('Corey', 'Schafer', 50000)
		self.emp_2 = Employee('Sue', 'Smith', 60000)

	def tearDown(self):
		pass


	def test_email(self):
		print('test_email')
		self.assertEqual(self.emp_1.email, 	'Corey.Schafer@email.com')
		self.assertEqual(self.emp_2.email,  'Sue.Smith@email.com')

		self.emp_1.first = 'john'
		self.emp_2.first = 'jane'

		self.assertEqual(self.emp_1.email, 'john.Schafer@email.com')
		self.assertEqual(self.emp_2.email, 'jane.Smith@email.com')

	def test_fullname(self):
		print('test_fullname')
		self.assertEqual(self.emp_1.fullname, 	'Corey Schafer')
		self.assertEqual(self.emp_2.fullname, 	'Sue Smith')

		self.emp_1.first = 'john'
		self.emp_2.first = 'jane'

		self.assertEqual(self.emp_1.fullname, 'john Schafer')
		self.assertEqual(self.emp_2.fullname, 'jane Smith')

	def test_apply_raise(self):
		self.emp_1.apply_raise()
		self.emp_2.apply_raise()

		self.assertEqual(self.emp_1.pay, 52500)
		self.assertEqual(self.emp_2.pay, 63000)


	def test_monthly_schedule(self):
		with patch('employee.requests.get') as mocked_get:
			mocked_get.return_value.ok = True
			mocked_get.return_value.text = 'Success'

			schedule = self.empl_1.monthly_schedule('May')
			mocked_get.assert_called_with('http://company.com.Schafer/May')
			self.assertEqual(schedule, 'Success')


			mocked_get.return_value.ok = False

			schedule = self.empl_1.monthly_schedule('Jane')
			mocked_get.assert_called_with('http://company.com.Smith/Jane')
			self.assertEqual(schedule, 'Bad Response')

if __name__ == '__main__':
	unittest.main()