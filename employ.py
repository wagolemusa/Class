class Employee:
	num_of_emps = 0
	raise_amount = 1.04

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
		self.pay = int(self.pay * self.raise_amount)



emp_1 = Employee('Corey', 'Schofar', 500000)
emp_2 = Employee('Test', 'User', 600000)

print(Employee.num_of_emps)

# print(emp_1.__dict__)

# # print(Employee.raise_amount)
# # print(emp_1.raise_amount)
# # print(emp_2.raise_amount)

# # print(emp_1.pay)
# # emp_1.apply_raise()
# # print(emp_1.pay)

# # print(emp_1.email)
# # print(emp_2.email)

# # print(emp_1.fullname())
# # print (emp_2.fullname())








