import datetime
class User:
	def __init__(self, full_name, birthday):
		self.name = full_name
		self.birthday = birthday

		#Extract first and last name
		name_prices = full_name.split(" ")
		self.first_name = name_prices[0]
		self.last_name = name_prices[-1]

	def age(self):
		today = datetime.date(2018, 8, 27)
		yyyy = int(self.birthday[0:4])
		mm = int(self.birthday[4:6])
		dd = int(self.birthday[6:8])
		dob = datetime.date(yyyy, mm, dd)
		age_in_days = (today - dob).days
		age_in_years = age_in_days / 356
		return int(age_in_years)

user = User("Refueg wise", "1234544")
print(user.age())
