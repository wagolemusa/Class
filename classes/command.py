users = {}
comment = {}
status = ""

def displayMenu():
	status = input("You ready a user? y/n? Post Press p, and Press q to quit")
	if status == "y":
		loginUser()
	elif status == "n":
		registerUser()
	elif status == "p":
		datas()
	elif status == "q":
		print("thanks for using the system")

def registerUser():
	firstname = input("\nEnter firstname")
	username = input("\n Enter username")
	email = input("\n Enter email")
	if username and email in users:
		print("\n username or email aleady exist: ")
	else:
		password = input("\n Enter password")
		users[username] = password
		print("\nUser created\n")

def loginUser():
	username = input("Enter username")
	password = input("Enter passward")

	if username in users and users[username] == password:
		print("\nLogin successfull!\n")
	else:
		print("\nUser doesn't exit\n")


def datas():
	title = input("\n Enter Title")
	connect = input("\n Enter your Connect")

while status != "q":
	displayMenu()








