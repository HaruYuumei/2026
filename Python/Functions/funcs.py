# python basic course

# Functions runs blocks of codes, they can return data as results 
# Functions can be used to avoid repeated codes

# to define a function you use the keyword def

def my_function():
    print("Hello World")

my_function()

# naming a function follows the same rules as the variables

# function1()
# _func()
# myFunc()

# functions can return data using the return keyword
# Once a function reaches the return keyword it will stop running 

def say_hello():
    return "Yoho!"

Hello = say_hello()

print(Hello)

# functions without return statements will return None as default

# just like Loops, Functions can't be empty, in case you need or have a empty function declared, you can use 
# the pass statement to skip it

# Functions with arguments
# you can define an argument on a function inside the parenthesis of the functions, there are no limit to the amount of arguments, aslong as you separate them with a comma

def print_name(name):
    print(name)

print_name("Saba")

# Argument vs Parameter

def fun(value): # value here is parameter
    print(value)

fun(5) # 5 here is a Argument

# The amount of parameters setted on a function is the same number of arguments necessary to call the func

def sum(a,b):
    print(a+b)

sum(5,4) # function needs 2 arguments, so it works
# sum(2) # doesn't work

#default values can be attributed to functions parameters, allowing to call functions without passing all the arguments

def mult(a,b=5):
    print(a*b)

mult(5,5)
mult(10)
# mult() won't work cuz it requires at least one value on argument

# default values can be ovverrided
def country(default="Brazil"):
    print(default)

country()
country("Norway")

# you can run functions with Key=Value arguments
sum(a=10,b=90)

# a function can recieve any kind of data, like lists, dicts

# Positions / kwargs  only functions can be defined with / and *

def name1(name,/):
    return name

def name2(*,name):
    print("Hello ",name)

name1("Emil")
# name1(name = "lord") #shouldn't work

name2(name="Yonnah")
# name2("Yonnah") #souldn't work

# you can combine both on same function too

def cal(a,b,/,*,c,d):
    print(a+b+c+d)

cal("Hello","World",c=" ",d="!")

# *args and **kwargs
# Both function as a wildcard, when you don't know how many parameters a function will need
# *args acts as a tuple, storing the info insde of it while **kwargs works as a dictonary

