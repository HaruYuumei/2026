

# Simple login System
#
# Account creation ->
# username ->
# Password ->
# verify account password ->

import os
isLogged = False

#creating file
if os.path.exists("Accounts.txt"):
    print("Account Log exists")
else:
    file = open("Accounts.txt","x")  
    print("Account logs created")  

#Opening and reading file  | not using this right now might delete it 
def open_datas():
    with open("Accounts.txt") as f:
        for x in f:
            print(f.readline())

# writing on the file
def write_data(**kwargs): # kwargs is a dictonary
    with open("Accounts.txt","a") as f:
        f.write(kwargs["username"])
        f.write(" : ")
        f.write(kwargs["password"])
        f.write("\n")

# write_data( user = username,password = password) # you pass the key and the value to the kwargs dictonary

def getUserInput():
    userInput = input()
    return userInput

# checking infos
def loginCheck(**kwargs):
    with open("Accounts.txt") as f:

        user = kwargs["username"]
        pwd = kwargs["password"]

        for rows in f:
            line = f.readline()
            l1 = line[0:len(user)]
            l2 = line[len(user)+3:] # +3 to skip the " : " from the line

            if user.strip() == l1.strip():
                if pwd.strip() == l2.strip():
                    print("proceed login")
                    isLogged = True
                    return isLogged
            else:
                print("invalid user/password")
        else:
            print("Unable to find User, please create an account")
            create_account() # I'm sending the create account now, it will be moved later to the create account page


# create account 
def create_account():
    username = None
    password = None

    print("please input the wished username:")

    while username == None: #loop for username check
        input = getUserInput()

        #check if username already exists:
        with open("Accounts.txt") as f:
            for rows in f:
                if input in rows: # there might be some bug here, need to change it
                    print("Username already in use, pick another one")
                    break
                else:
                    username = input
                    break
                   
    print("Now please type your wished password:")
    while password == None: # loop for password
        
        input = getUserInput()

        #check if password matches security test
        if len(input) < 5:
            print("Password must have at least 5 inputs")
            print("type again")
        else:
            password=input
            break
        
    write_data(username=username,password = password)
    print("Account Created!, please login:")
    




while not isLogged:

    userinfo :dict[str,str] = {}
    print("#======================#") #22
    print("#=        Login       =#")
    print("#======================#")
    print("#=   Type your user:  =#")
    
    userInput = getUserInput()
    userinfo["username"] = userInput
    
    print("#= Type your password:=#")
    userInput = getUserInput()
    userinfo["password"] = userInput

    print("#=   Checking Infos   =#")
    isLogged = loginCheck(username = userinfo["username"], password=userinfo["password"])

    