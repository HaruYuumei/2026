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



# you can get the type of a variable using: type(variable)

singer = "yorushika"
song_lenght = 4.36
awesome = True

print(type(singer),type(song_lenght),type(awesome))


# STR data type
# any text attributed to a variable is considered a str type data

name = "jonas"
surname = 'Brothers'
print(name + surname)

# Numeric types:
# int = integer type, any integer number value

x = 10
y = -15
z = 6490

# float = any  floating point number

a = 1.4
b = 0.3

# complex
# a number that consist of its real and imaginary part, indicated by adding j at the end

c = 6j

# Sequence types

# tuples are imutable data types that can hold multiple information, but cannot be changed

d = (8,9)
e = ("hide on bush","champion", 1337)

# you can read tuple values

print(d[0])
print(e[0]," ",e[2])

xx,yy = d
print(xx,yy)

# Lists = are ordered collections of data, that are mutable and can hold any type of data

numbers = [0,1,2,3,4,5,6,7,8,9]
for i in numbers:
    print("Even number: ",i) if i % 2 == 0 else print("Odd number: ", i) 

# you can access values in lists from each side
print(numbers[0]) # 0
print(numbers[-1]) # 9

# you can add or insert values in lists using built-in functions
names = [] # declaring a empty list

names.append("Nines")

print(len(names)) # this should show 1 lenght
print(names[0])

names.insert(1,"Commander White")
print(len(names))   # this should show 2 lenght
print(names[0], names[1])

# nines and Commander White  are both on spot 0 and 1, I can use insert to insert a name between them, changing Commander White to position 2
names.insert(1,"2b")
print(len(names))   # this should show 3 lenght

for i in range(0,len(names)): # for index in range(start = 0, end= lenght of names[])
    print(f"{i}:{names[i]}")    # print (index:name inside index value)

# You can remove values from lists too with a built-in function

# names.remove("name")
# names.pop() removes the last item
# names.pop(index) remove specific list item using index

names.pop(2)
for i in range(0,len(names)):
    print(f"{i}:{names[i]}")

# Slicing lists, you can slice a list, this creates a new list without editing the original one

print(numbers[0:5])
print(numbers[5:10])


# range = we been using on for loops here, range simply determine a range of values

# range(start,stop)
for range_numbers in range(0,10):
    print(range_numbers)

for even_numbers in range(0,25):
    print(even_numbers) if even_numbers % 2 == 0 else None

for backward_numbers in range(10,0,-1): # going downwards
    print(backward_numbers)




