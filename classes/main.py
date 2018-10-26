users = {}
status = ""

def displayMenu():
	status = input("Are you registered user? y/n Press q to quit")
	if status == "y":
		oldUser()
	elif status == "n":
		newUser()

def newUser():
	createLogin = input("create login: ")
	if createLogin in users:
		print("\nLogin name already exit!\n")
	else:
		createPassw = input("create password: ")
		users[createLogin] = createPassw
		print("\nUsers Created\n")

def oldUser():
	login = input("Enter login name: 	")
	passw = input("Enter passward: ")
	if 	login in users and users[login] == passw:
		print("\n Login successfull!\n")
	else:
		print("\nUser doesn't exist or wrong passward!\n")

while status != "q":
	displayMenu()