# This is a comment
print("Hello World")

# Primitive data type
# There is no data type all are basicaly an object

# Kinds of Primitive datatype
# Integers
# Float
# String
# Complex

# Examples

# Integer
a = 2;
print(type(a))


# Float
a = 1.3
print(type(a))

# String 
a = "Aditya Pathak"
print(type(a))

# Complex
a = 5j
print(type(a))

# Variable or Identifiers
# Name can start with char and _ but not with no's
# Eg: a, b, _ab, _a23n
_ab90 = 45
print(_ab90)

# String Concatination
first_name = "Aditya"
last_name = "Pathak"
print("Hello Mr {}, {}".format(first_name, last_name))

# (end and sep)
# Adding Seperator
print("Aditya", "Pathak", "Web-Developer", "Programmer", sep=' , ')

# Adding End Line char by default \n is there
print("hello")
print("world")
# Adding a new end line char
# print("Hello" end=';')
print("world")

# Taking Input from user
# input() function is used
# alwys returns a string

b = input()
print(b)
print(type(b))

# Typecasting
# Converting to specific datatype
c = int(input())
print(c)
print(type(c))

d = complex(input())
print(d)
print(type(d))