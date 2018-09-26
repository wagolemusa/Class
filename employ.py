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

	#classmethods to add new user 
	@classmethod
	def from_string(cls, emp_str):
		first, last, pay = emp_str.split('-')
		return cls(first, last, pay)

	#static method to vaildate working days
	@staticmethod
	def is_workday(day):
		if day.weekday() == 5:
			print ("Its working day time for worker")
		elif day.weekday() == 6:
			print ("Its weekend")
		else:
			print ("We will call you")

#class developer and inheritance the Employee class
class  Developer(Employee):
	raise_amt = 1.10
	def __init__(self, first, last, pay, prog_lang):
		super().__init__(first, last, pay)

		self.prog_lang = prog_lang	

dev_1 = Developer('Corey', 'Schofar', 500000, 'python')
dev_2 = Developer('Test', 'User', 600000, 'java')



print(dev_1.email)
print(dev_1.prog_lang)


# print(help(Developer))
# print(dev_1.email)
# print(dev_2.email)

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)









