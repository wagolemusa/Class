class Employee:
	def __init__(self, first,last,pay):
		self.first = first
		self.last = last
		self.pay = pay

	@property
	def email(self):
		return '{}.{}@mail.com'.format(self.first, self.last)

		# method to dispaly fullname
	@property
	def fullname(self):
		return  '{} {}'.format(self.first, self.last, self.pay)

	@fullname.setter
	def fullname(self, name):
		first, last = name.split(' ')
		self.first = first
		self.last = last

	@fullname.deleter
	def fullname(self):
		print('Delete Name!')
		self.first = None
		self.last = None


emp_1 = Employee('John', 'Smith', 50000)

emp_1.fullname = 'refuge wise'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)
print(emp_1.pay)

del emp_1.fullname




