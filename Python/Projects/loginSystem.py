

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
        f.write(kwargs["username"]+":"+kwargs["password"]+"\n")

# write_data( user = username,password = password) # you pass the key and the value to the kwargs dictonary

# checking infos
def loginCheck(**kwargs):
    with open("Accounts.txt") as f:

        user = kwargs["username"]
        pwd = kwargs["password"]

        for rows in f:
            
            line = rows
            lineInfo = line.split(":")

            if user.strip() == lineInfo[0].strip():
                if pwd.strip() == lineInfo[1].strip():
                    print("proceed login")
                    return True
                else:
                    print("Invalid password")
                    break
        else:
            print("Unable to find User")
            create_account() # I'm sending the create account now, it will be moved later to the create account page



# create account 
def create_account():
    username = None
    password = None

    print("please input the wished username:")

    while username == None: #loop for username check
        user = input()

        #check if username already exists:
        with open("Accounts.txt") as f:
            for rows in f:
                
                line = rows
                lineInfo = line.split(":")
                
                if user == lineInfo[0].strip():
                    print("Username already in use, pick another one")
                    break
                elif ":" in user:
                    print("usernames must have only leters and numbers")
                    break
                elif " " in user:
                    print("usernames must have only letters and numbers")
                    break
            else:
                username = user
                break

                   
    print("Now please type your wished password:")
    while password == None: # loop for password
        
        pwd = input()

        #check if password matches security test
        if len(pwd) < 5:
            print("Password must have at least 5 inputs")
            print("type again")

        else:
            password=pwd
            break
        
    write_data(username=username,password = password)
    print("Account Created!, please login:")
    




while not isLogged:

    userinfo :dict[str,str] = {}
    print("#======================#") #22
    print("#=        Login       =#")
    print("#======================#")
    print("#=   Type your user:  =#")
    
    userInput = input()
    userinfo["username"] = userInput
    
    print("#= Type your password:=#")
    userInput = input()
    userinfo["password"] = userInput

    print("#=   Checking Infos   =#")
    isLogged = loginCheck(username = userinfo["username"], password=userinfo["password"])

    