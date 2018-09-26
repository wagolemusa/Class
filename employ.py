class Employee:
	num_of_emps = 0
	raise_amt = 1.04

	def __init__(self, first,last,pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@company.com'

		Employee.num_of_emps += 1

		# method to dispaly fullnames
	def fullname(self):
		return  '{} {}'.format(self.first, self.last)

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amt)

	@classmethod
	def set_raise_amt(cls, amount):
		cls.raise_amt = amount

emp_1 = Employee('Corey', 'Schofar', 500000)
emp_2 = Employee('Test', 'User', 600000)

emp_str_1 = 'john-Deo-70000'

first, last, pay = emp_str_1.split('-')

new_emp_1 = Employee(first, last, pay)

print(new_emp_1.email)
print(new_emp_1.pay)

# Employee.set_raise_amt(1.05)
# print(Employee.raise_amt)
# print(emp_1.raise_amt)
# print(emp_2.raise_amt)

print(Employee.num_of_emps)









