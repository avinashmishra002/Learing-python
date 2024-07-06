#   Syntax
print("start")





# Variables

name = "shonu"   
age = 23 
salery = 10.22 


print(name,age)


x = str("abcd")    
y = int(12345)    
z = float(3.02)


print(x,y,z)

# Variable Names

# valid name meanigfull


# Legal variable names:

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"


# Camel Case
# Each word, except the first, starts with a capital letter:

myVariableName = "John"
# Pascal Case
# Each word starts with a capital letter:

MyVariableName = "John"

# Snake Case
# Each word is separated by an underscore character:

my_variable_name = "John"


# no use symbols  !,@,#,%,$,%   identifier




# Data Types

# In programming, data type is an important concept.

# Variables can store data of different types, and different types can do different things.

# Python has the following data types built-in by default, in these categories:

# Text Type:	str
# Numeric Types:	int, float, complex  
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType




# type() function

hii = 'hello'
print(type(hii))      




# x = "Hello World"	str	
# x = 20	int	
# x = 20.5	float	
# x = 1j	complex	
# x = ["apple", "banana", "cherry"]	list	
# x = ("apple", "banana", "cherry")	tuple	
# x = range(3)	range	
# x = {"name" : "John", "age" : 36}	dict	
# x = {"apple", "banana", "cherry"}	set	
# x = frozenset({"apple", "banana", "cherry"})	frozenset
# x = True	bool	
# x = b"Hello"	bytes	
# x = bytearray(5)	bytearray	
# x = memoryview(bytes(5))	memoryview	
# x = None	NoneType

 


# Numeric Types:

# int: Integer, e.g., 42
myAge = 20
print(type(age))
# float: Floating point number, e.g., 3.14
# complex: Complex number, e.g., 1 + 2j
# Sequence Types:

# str: String, e.g., "hello"
# list: List, e.g., [1, 2, 3]
# tuple: Tuple, e.g., (1, 2, 3)
# range: Range, e.g., range(5)
# Mapping Type:

# dict: Dictionary, e.g., {"key": "value"}
# Set Types:

# set: Set, e.g., {1, 2, 3}
# frozenset: Immutable set, e.g., frozenset([1, 2, 3])
# Boolean Type:

# bool: Boolean, e.g., True or False
# Binary Types:

# bytes: Bytes, e.g., b'hello'
# bytearray: Byte array, e.g., bytearray(b'hello')
# memoryview: Memory view, e.g., memoryview(b'hello')
# None Type:

# NoneType: The type of the None object, used to signify absence of value
# These built-in types form the core of Python's type system.


# type Casting
 #1 
Myage = 25

print(type(Myage))


ageFloat = float (Myage)

print(type(ageFloat))

ageFloat = complex (Myage)

print(type(ageFloat))  

 #2 
f = float ("5")
h = 2.05
print(type(f)) 

print (f + h)

#3
str = str ("1234")
print(type(str))


 # Input

name = input("enter your name:")  #string type

print("welcome",name)

val = int(input("enter some value:"))  # int type
print(type(val), val)


name = input("enter your name:")
age = int(input ("enter your age:"))
marks = float(input("enter your marks:"))

print('welcome', name)
print("your age ",age)
print("your marks", marks)


#practice
# input sum

first = int(input("enter number: "))
second = int(input("enter number: "))
print(first + second)

#  square size

size = int(input("enter size :"))
print("area =", size*size)

a = 1
b = 100

x = range(a , b)

print(x)
