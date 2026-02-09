# Access control

userAge = int(input("Type your age: "))
userPassword = input("password... ")
isAdmin = input("Are you and Admin? yes / no ")

if userPassword == "python123" and (userAge>=18 or isAdmin == "yes"):
    print("Full access granted")
else:
    print("Access Denied")
