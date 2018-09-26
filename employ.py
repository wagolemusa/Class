class Employee:

	raise_amt = 1.04

	def __init__(self, first,last,pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@company.com'

		# method to dispaly fullname
	def fullname(self):
		return  '{} {}'.format(self.first, self.last)

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amt)

	#it was design to be seen by Developers
	def __repr__(self):
		return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

	#it was desigin to be seen by users, Which means it displays
	def __str__(self):
		return '{} - {}'.format(self.fullname(), self.email)

	def __add__(self, other):
		return self.pay + other.pay

	def __len__(self):
		return len(self.fullname())
          

emp_1 = Employee('Corey', 'Schofar', 500000)
emp_2 = Employee('Test', 'User', 600000)

print(len(emp_1))

# print (emp_1 + emp_2)

# # #print(emp_1)

# # print(repr(emp_1))
# # print(str(emp_2))



