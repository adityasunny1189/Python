# class Student:
# 	__passingPercentage = 45

# 	def __init__(self, name, rollno):
# 		self.__name = name
# 		self.rollno = rollno

# 	def printDetails(self):
# 		print("Name: ", self.__name)
# 		print("RollNo: ", self.rollno)

# 	@staticmethod
# 	def isTeen(no):
# 		if no > 16:
# 			print("is Teen")
# 		else:
# 			print("Not Teen")


# s1 = Student("aditya", 19)

# s1.printDetails()

# print(s1._Student__name)

# s2 = Student.isTeen(13)


# Inheritance

class vehicle:

	def __init__(self, color, maxSpeed):

		self.color = color
		self.maxSpeed = maxSpeed

class Car(vehicle):

	def __init__(self, color, maxSpeed, numGears, natureFriendly):

		super().__init__(color, maxSpeed)

		self.numGears = numGears
		self.natureFriendly = natureFriendly

	def printCarDetails(self):

		print("Color: ", self.color)
		print("Max Speed: ", self.maxSpeed)
		print("Num of Gears: ", self.numGears)
		print("Nature Friendly: ", self.natureFriendly)

c1 = Car("black", 200, 8, True)
c1.printCarDetails()

