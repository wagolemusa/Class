import datetime

class Person:
	def __init__(self):
		self.name =  input("\n name\n")#name
		self.username = input("\n username\n")
		self.birthdate = int(input("\n birthdate\n"))
		self.address = input("\n address\n")
		self.telephone = int(input("\n telephone\n"))
		self.email = input("\n email\n")


	def age(self):
		today = datetime.date.today()
		age = today.year - self.birthdate.year

		if  today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
			age -= 1
		return age

	def showData(self):
		return '{} {} {} {} {}'.format(self.name, self.username, self.birthdate, self.address, self.telephone, self.email)
# person = Person(
#     "Jane",
#     "Doe",
#     datetime.date(1992, 3, 12), # year, month, day
#     "No. 12 Short Street, Greenville",
#     "555 456 0987",
#     "jane.doe@example.com"
# )

# print(person.name)
# print(person.email)
# print(person.age())

reg = Person()
print(reg.showData())