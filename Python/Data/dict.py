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


# Dictonary

# A dictonary stores values as: key->value, Like a real world dictonary where you have word->definition

player = {
    "userName" : "Ren",  # KEY : Value
    "age" : 18,
    "role" : "Healer"
}
# To read a dictonary value you don't Index it, you get the KEY instead

print(player["userName"]) # display username

# You can add, modify or delete info, always remember to use KEYs

player["weapon"] = "Greatsword"
print(player["weapon"])

print(player["age"])
player["age"] = 20
print(player["age"])

player["city"] = "Tokyo"

if "city" in player:
    print("there is a location")
else:
    print("No location found")


print(player["city"])
del player["city"]
print("Location deleted")


if "city" in player:
    print("there is a location")
else:
    print("No location found")


# you can check if a KEY exists inside a dictonary like we did up here

if "age" in player:
    print(player["age"])

# Looping inside a dictonary:

for key in player:  #Getting the KEYs inside a dictonary
    print(key)

for value in player.values(): # Getting the VALUES inside a dictonary
    print(value)

#pattern loop, mostly used everywhere
for key,value in player.items():    #Getting both KEY:VALUE inside a dictonary
    print(key,":",value)


#now the hard part, nested dictonary:

# lets say i want to build a inventory, that inventory is a dictonary with slots, each slots holds an Item, an Item is also a dictonary

item: dict[str,str]={  # Items should have a name, a value and a description
    "name":"",
    "value":"",
    "description":""
}

copper_sword = item # creating an Item called copper_sword and setting its attributes
copper_sword["name"] = "copper sword"
copper_sword["value"] = 10
copper_sword["description"] = "A simple forged copper sword"



inventory : dict[str,any] = {
    "slot0": any,
    "slot1": any,
    "slot2": any,
    "slot3": any,
    "slot4": any,
    "slot5": any,
    "slot6": any,
    "slot7": any,
    "slot8": any,
    "slot9": any,
}

player_inventory = inventory # creating a player inventory

player_inventory["slot0"] = copper_sword # attributing item to slot0

for key,value in player_inventory.items(): 
    print(key,":", value)


# you can add nested dictonaries too
player["stats"] = {
    "hp" : 100,
    "str" : 20,
    "dex" : 17
}

print("Player Strenght level: ",player["stats"]["str"])

