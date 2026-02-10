
# A simple Calculator project

# Get user input -> ok
# Select Operation -> ok
# Calculate and Return value -> ok
# ASCII Menu -> Ok
#
# This is a WIP and there are no erro checking except divide by 0 one
# Exit by ctrl C
#

# Sum
def sum(a = 0,b = 0):
    return a+b

# Subtract
def sub(a = 0,b = 0):
    return a-b

# divide
def div(a = 0,b = 0):
    return a/b if b != 0 else print("#===== Can't divide  by Zero =====#")

# multiply
def mult(a=0,b=0):
    return a*b

def getUserInput():
    return float(input())



print("#============ Welcome ============#") #34
running = True
while running:
    print("#=================================#") 
    print("#=================================#")  
    print("#===  Input the  first Number  ===#")
    number1 = getUserInput()
    print("#===  Input the second Number  ===#")
    number2 = getUserInput()

    #select operation
    print("#===== Select  the operation =====#")
    print("#===== 1-Add,     2-Subtract =====#")
    print("#===== 3-Divide,  4-Multiply =====#")
    
    selection = getUserInput()
    
    match selection:
        case 1:
            print(sum(number1,number2))
            
        case 2: 
            print(sub(number1,number2))
            
        case 3:
            print(div(number1,number2))
            
        case 4:
            print(mult(number1,number2))