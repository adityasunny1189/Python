# import json
with open("users.txt") as myfile:
	users = myfile.read()

def login_function():
	print("Enter username: ", end = "")
	user = input()
	if user in users:
		# print("PassWord: ", end = "")
		# password = input()
		# if users[user] == Password:
		print("Welcome %s"%(user))
		# else:
			# print("Wrong password")
	else:
		print("Invalid User")


def signup_function():
	print("Enter a username: ", end = "")
	user = input()
	global users
	if user not in users:
		with open("users.txt", "a") as myfile:
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