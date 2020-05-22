# myfile = open("textfile.txt")
# file_content = myfile.read()
# myfile.close()
# print(file_content)
# print(fruits)
with open("textfile.txt") as myfile:
	file_content = myfile.read()
fruits = file_content.split()
print("Enter fruit name:", end = " ")
fruit = input()
if fruit in fruits:
	print("Yeah you can buy")
else:
	print("piss off")



# Another way is using with
# with open("textfile.txt") as myfile:
# 	file_content = myfile.read()
	# No need to apply the close method as it will close automatically