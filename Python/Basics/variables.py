# python introduction course

# Variables

# Python does not have a variable declaration like other programming languages
# A variable will be created in the moment you assign a value to it

variable_a = 0
variable_b = "John Python"

# You can use the Print function to show on the console the value of the variable

print(variable_a)
print(variable_b)

# You can use the print(f" ") to display variables direct on the message
print(f"Welcome {variable_b}, Hope you have a wonderful day!") 

#Variables don't need to be assigned a specific typr, and can be changed to other types later in the program

print("Variable A value is: ",variable_a)
variable_a = "John notAIntegerAnymore"
print("Variable A value now is: ",variable_a)

# You can specify the type of a variable by what is called CASTING

variable_int = int(10)
variable_float = float(10)
variable_str = str(10) # this one is a str variable, when printing it will not show the ""/' '

print("Showing the values: ",variable_int, variable_str,variable_float)

# you can get the type of the variable you want, using the pre-made function type(args)
print(type(variable_int))
print(type(variable_str))

# Variables are case sensitive
variable_c = 35
Variable_c = "female"
print(variable_c, Variable_c) # not the same thing
print(type(variable_c),type(Variable_c))

# When declaring a variable, notice that you Cannot give the name of the variable starting with a number, You also can't have - or spaces in the name
# Use letters, numbers and _ on naming a variable

# 3myvar = value  // wrong
# my var = value // wrong
# my-var = value // wrong


# Declaring variables with confusing names can make the code readbillity bad.
# So stick to using camelCase, PascalCaseType or snake_case_type

# You can assign multiple values to multiple variables
variable_d,variable_e,variable_f = 1,2,3
print(variable_d,variable_e,variable_f)

# the same value for multiple variables also works!
var_g = var_h = var_i = "names"

print(var_g,var_h,var_i)

# Variables created outside a function (like all the ones we did here) are considered Global variables
# This means that they can be used by everyone, both inside and outside
# If you create a variable inside a function, by default that variable is declared as local variable
# You can use the keyword global to declare a variable inside a function as global variable

# To change a global variable value inside a function, refer to the variable using the global keyword

