class Employee:
	def __init__(self, first,last,pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@company.com'

		# method to dispaly fullname
	def fullname(self):
		return  '{} {}'.format(self.first, self.last)
          

emp_1 = Employee('Corey', 'Schofar', 500000)
emp_2 = Employee('Test', 'User', 600000)


print(emp_1.email)
print(emp_2.email)

print(emp_1.fullname())
print (emp_2.fullname())




