class Employee:


	def __init__(self):
			self.firstname = input("Enter fristname")
			self.username = input("Enter username")
			self.lastname = input("Enter lastname")
			self.email = input("Enter Email")
			self.store = []

	def showname(self):
		return '{} {}'.format(self.firstname, self.username)




reg = Employee()
print(reg.showData())