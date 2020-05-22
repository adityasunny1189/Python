import json 

with open("data.json", "r") as file:
	data = file.read() # read() reads the json file and convert it to string
	print(type(data))
	users = json.loads(data) # loads converts string to dictionary

print(users["adityasunny1189"])
print(type(users))
print(type(list(users.keys())))
# json.load(): json.load() accepts file object, 
# parses the JSON data, populates a Python dictionary 
# with the data and returns it back to you. 