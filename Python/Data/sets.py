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


# Set/frozenset


# Set is an unordered collection
# It contains only UNIQUE items

numbers = {1,3,4,5,6,5,4,7,9}
print(numbers) #there wont be more than one 4,5

# sets are mutables
numbers.add(20)
print(numbers) 

#notice how the number will be put not in order (it might sometimes), thats just how the set works, for it to be faster than lists and other 
# it doesn't take in consideration the position on the placement

# to remove a value is simple too
numbers.remove(9) #not safe if there is no number 9 on the set
numbers.discard(9) # safe if there is no number 9 on the set

numbers.clear() # to clear the set


#set operations
a = {1,2,3,4,5,6}
b = {5,6,7,8}
print(a | b) # union

print( a & b ) # Intersection

print( a - b ) # difference
print( b - a )

print( a ^ b ) # symmetric difference


# Frozenset is equal a set, the difference is: frozenset is Immutable, you can't add or remove items from it
# then why use it/exists = because dictonary KEYs cant be mutable.

permission = {
    frozenset(["read","write"]): "editor", # a set with read and write  = editor
    frozenset(["read"]): "viewer" # a set with only read = viewer
}   

user = {"read"} # user is a set() and recieve the "read" value
user_key = frozenset(user) # converts user set to frozenset()
role = permission.get(user_key,"unkown") # role = value of the dictonary key that matches the user value
print(role) # shows user role





