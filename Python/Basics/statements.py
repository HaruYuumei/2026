# python introduction course

# Statements are controllers to check conditions

# /if/ is the most known statement it checks if (duh!) something matches the requirements

x = 10

if x == 10:
    print("X is ten!")

# python uses the logical conditions from mathematics
# Equals: ==
# Not Equal: !=
# Less than <
# Greater than >
# Less or Equal <=
# Greater or Equal >=

y = 5
print(f"Y is {y}")

if x < y:
    print("Y is Bigger!")
if x > y:
    print("X is Bigger!")

# The If statement valuates the condition and returns either TRUE or FALSE, if the condition is TRUE, it runs whatever is inside the block
# if the condition is FALSE, it will skip the block of code
# pay attention to de identation

# This is correct:
# x = 10
# if x == 10:
#   print("X is ten")

# This is wrong!
# x = 10
# if x == 10:
# print("X is ten")


# You can have multiples statements inside a block
age = 18

if age >= 18:
    print("You are an adult")
    print("You can vote")
    print("You can do whatever you set your mind to!")

# ELIF

# Elif comes in in case the previous condition where not meet
# if that condition didn't work, try this one = Elif (else if)

var_a = 10
var_b = 6

if var_a < var_b:
    print("A is smaller")
elif var_b < var_a: #if the previous condition didn't met, try this one
    print("B is Smaller")

# You can have multiple statements, python will try each one untill it find the first correct one

var_grade = 75

if var_grade >= 90:
    print("A")
elif var_grade >= 80:
    print("B")
elif var_grade >= 60:
    print("C")
elif var_grade >= 40:
    print("D")
elif var_grade >= 20:
    print("E")
elif var_grade >=10:
    print("F")


# ELSE

# The else statment runs when none of the previous statements returned True
# if none of these works then do this =  ELSE

var_number1 = 100
var_number2 = 34

if var_number2 > var_number1:    # var_number1 is bigger
    print("Number2 is bigger")
elif var_number1 == var_number2:    # They are not equal
    print("They are both equal")
else:                               # Since none of the above returned true, do this:
    print("Number 2 is Smaller")


# Short hand if

# sometimes you only have one statemente to execute, for that you can simplify the if statement like this:

var_z = 10
var_y = 50

if var_z < var_y :print("Z is smaller than Y")

# The same can be done with if else statements

print("Z is Bigger") if var_z > var_y else print("Z is smaller")

# you can assign values to variables this way too

k,l = 7,5
m = k if k>l else l 
print(f"M value is : {m}")

# You can add multiples statements like this too, but keep it short so the code is readable

var_c = 300
var_d = 500
print("C") if var_c>var_d else print("=") if var_d==var_c else print("D") #print C if C is bigger = if both are equal or D if D is bigger


# LOGICAL OPERATORS

# Python uses the basic logical operators AND OR NOT 

# AND operators serves to check if the statements are BOTH  right

v_a = True
V_b = True
if v_a and V_b:
    print("Both are true")

# OR operator checks if AT LEAST one of the requirements are right

v_c = False
if v_a or v_c:
    print(" At least one is Right")

# NOT operator changes the check to the oposite type

#if v_A is True = no print
#if v_a is False = print
if not v_a:
    print("Printing")  # this wont trigger because v_A = True


