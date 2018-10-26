users = []

def register():
	firstname = input("Enter first name")
	username = input("Enter username")
	email = input("Enter Email")
	password = input("Enter Password")

	Data = ({"firstname": firstname, "username":username, "email":email, "password":password})
		# # users.append(firstname, username, email, password)
	for row in Data:
		users.append(Data)
			# firstname = row[0]
			# username = row[1]
			# emai = row[2]
			# password = row[3]
		# users.update(Data)
		print(row)

def login():
	username = input("Enter username")
	password = input("Enter password")
	if username in users:
		if password in users:
			return "You are succefully logged In"
	return "Wrong Users"

reg = register()
