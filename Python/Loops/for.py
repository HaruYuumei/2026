#basic python course


# LOOPS
# While
# For



# FOR LOOPS

# for loops is used for iteration over a sequence

shopping_cart = ["Apples","Beer","Chocolate","Meat"]

for items in shopping_cart:
    print(items)

# for loops does not requires index variable beforehand!

# looping through a string

word = "banana"
for letters in word:
    print(letters)

# the break statement stops the loop, even mid through

for items in shopping_cart:
    print(items)
    if items == "Beer":
        print("HELL YEAH! BEER")
        break

# the continue statement continues a paused block

for item in shopping_cart:
    print(item)
    if item == "Chocolate":
        print("omg I love Chocolate!") # the program stop the iteration and continues to iterate
        continue
        
# the Range() function

# Range(value) returns a set of values starting from 0 initially

for x in range(9):
    print(x)

# you can change the starting value of range function aswell
for x in range(10,20): # starts at 10 goes till 19
    print(x)

#incrementing function

for x in range(0,11,2):
    print(x)

# Else statement runs after the loop ended

for x in range(1,100,10):
    print(x)
else:
    print("woa thats a lot of numbers")


# NESTED LOOPS!

# nets loops is when you have two loops, one inside the other
# the inner loop will execute once every outer loop iteration

x,y = 0,0

for posX in range(10):
    for posY in range(10):
        print(f"X: {posX}, Y: {posY}")

# the pass statment is used for when a loop is empty (loops cannot be created as empty) the pass statment make it skip the loop