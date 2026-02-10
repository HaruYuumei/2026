# Python introductory course

# Data Types

# Variables can hold multiple types of data
# Python has default data types already build in

# Text type data: str
# Numeric types: int, float, complex
# Sequence types: tuples,list,range
# Mapping types: dictonary
# set type : set, frozenset
# Boolean: bool
# binary: bytes,bytearray,memoryview
# none type: NoneType


# Boolean types are easy, there is only two states TRUE or FALSE, thats it

isTrue = True
isFalse = False

if isTrue:
    print("true")
if isFalse: # wont print because isFalse == False
    print("False")


# byte is a bit, a number from 0 to 255
# bytes are immutable

data = bytes([72,89,95]) # the numbers here are ASCII code
print(data) 

#multiple ways to create bytes

b1 = b"Hey"
b2 = bytes([24,25,26])
b3 = bytes(7)

# bytes are Immutable, they can't be changed or alterated

# bytearray are different, they are mutable

hello_data = bytearray(b"Hello World")
print(hello_data)
hello_data[9] = 32
print(hello_data)

#adding and modifying:
hello_data.append(33)
hello_data.extend(b"!@$")
print(hello_data)

# Memory view

# memoryview is a way to see binary data without copying it and even modify it but you can only modify if the data viewd is mutable

newdata = bytearray(b"abcde")
slice(newdata[0:2]) #slice makes a copy of the data, making the process slower

datas = bytearray(b"abc")
view = memoryview(datas)
view[0:2] = b"XY"
print(datas)

# NONE type

# None represents nothing, a data with nothing, a object with nothing, it does not mean 0 or empty, it means nothing

x = None # X has nothing on it
print(type(x))

username = "" # username is empty, it has something and that something is empty, but not nothing
print(type(username)) 

