import json
with open("users.json") as myfile:
	data = myfile.read()
	users_list = json.loads(data)

users = list(users_list.keys())

def login_function():
	print("Enter username: ", end = "")
	user = input()
	if user in users:
		print("Enter PassWord: ", end = "")
		password = int(input())
		if users[user] == password:
			print("Welcome %s"%(user))
		else:
			print("Wrong password")
	else:
		print("Invalid User")


def signup_function():
	print("Enter a username: ", end = "")
	user = input()
	global users
	if user not in users:
		with open("users.json", "a") as myfile:
			users = myfile.write("\n" + user)
			print("Username added please login now")
			print(users)
	else:
		print("username already present enter another name")

print("Do you want to login or signup:", end = " ")
choice = input()
if choice == "login":
	login_function()
elif choice == "signup":
	signup_function()
else:
	print("Invalid Option")