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

# Conditionals (if, elif, else)
var1 = 10
var2 = 10
if var1 > var2:
	print("Var1 is greater")
elif var1 == var2:
	print("both are same")
else:
	print("var2 is greater")

# Looping Statement
# while
print("While loop")
var3 = 10;
while var3 > 0:
	print(var3)
	var3 -= 1

# for
# as in c++ or another language for loop takes 3 args
# one is initialisation then condition and then increment/decrement
# but in python for loop takes iterable means they can iterate over 
# every element of the given thing say array for example
# for loops in python works on the principle of decomposition
# which means that if any thing can be decomposed into multiple thing
# then we can apply for loop on that
print("For Loop")
for i in [1, 2, 3, 4, 5]:
	print(i)

# even string can be decomposed so we can apply for loop over it
string = "Aditya"
for char in string:
	print(char)
# so basically it breaks the given thing into its atomic elements and iterate over it

# range() function
# it is also iterable 
# means for example if we give range(10) it means
# that we go from 1 to 10
for j in range(5):
	print(j)

# challenge 1
# print the pattern
# 55555
# 54445
# 54345
# 54445
# 55555

# break and continue behaves as same in python as in other language
# another statement is pass 
# what it does is that if there is a block say if and we want to write
# its code later then we give a pass statement so that interpreter
# simply passes over it ignoring it 
# otherwise it will be a wrong syntax
i = 10
if i > 10:
	pass
print("Just passed the previous if statement")
print("hell yeah")