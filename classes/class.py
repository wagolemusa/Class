class Employee:


	def __init__(self, firstname,username):
			self.firstname =  firstname #input("Enter fristname")
			self.username = username #input("Enter username")
			# self.lastname = lastname #input("Enter lastname")
			# self.email = email #input("Enter Email")

	def showname(self):

		return '{} {}'.format(self.firstname, self.username)


reg = Employee('refuge', 'wise')
print(reg.showname())